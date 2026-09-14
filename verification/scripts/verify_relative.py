# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Mangesh Raut

"""Offline relative-window diagnostics, exact unless explicitly labelled.

No external dependencies. Finite checks corroborate RELATIVE_WINDOWS.md;
they are not a proof of the ultimate asymptotic assertion.
"""

from fractions import Fraction as F
from itertools import product
from math import cos, sin, pi, ceil, log, sqrt
from random import Random
import json


def interval_counts(bits):
    n, m = len(bits), sum(bits)
    prefix = [0]
    mask = 0
    for i,bit in enumerate(bits):
        prefix.append(prefix[-1]+bit)
        mask |= bit << i
    phi = 0
    for y,bit in enumerate(bits):
        if bit:
            lo=max(0,2*y-n+1,(y+1)//2)
            hi=min(n-1,2*y,(n-1+y)//2)
            if lo <= hi:
                phi += prefix[hi+1]-prefix[lo]
    sigma = four = m
    for d in range(1,(n-1)//3+1):
        triple=mask & (mask>>d) & (mask>>(2*d))
        sigma += (triple & ((1<<(n-3*d))-1)).bit_count()
        sigma += (triple>>d).bit_count()
        four += 2*(triple & (mask>>(3*d))).bit_count()
    return phi,sigma,four,max(abs(n*prefix[i]-m*i) for i in range(n+1))


def interval_exhaustive():
    total=free=0
    for n in range(1,15):
        groups={m:[0,0,0,0] for m in range(n+1)}
        c=(n*n+2)//3
        for bits in product((0,1),repeat=n):
            m=sum(bits)
            phi,sigma,four,disc=interval_counts(bits)
            assert abs(n*n*phi-m*m*c) <= 4*m*n*disc
            if n<=7:
                direct_phi=direct_sigma=direct_four=0
                for x in range(n):
                    for d in range(-n,n+1):
                        if 0<=x+3*d<n:
                            direct_phi += bits[x+d]*bits[x+2*d]
                            direct_sigma += bits[x]*bits[x+d]*bits[x+2*d]
                            direct_four += bits[x]*bits[x+d]*bits[x+2*d]*bits[x+3*d]
                assert (phi,sigma,four)==(direct_phi,direct_sigma,direct_four)
            groups[m][0]+=1;groups[m][1]+=phi;groups[m][2]+=sigma;groups[m][3]+=four
            total+=1; free+=four==m
        for m,(count,phi_sum,sigma_sum,four_sum) in groups.items():
            a=F(m,n)
            def falling_ratio(j):
                if n<j: return F(0)
                out=F(1)
                for k in range(j): out*=F(m-k,n-k)
                return out
            r2,r3,r4=(falling_ratio(j) for j in (2,3,4))
            assert F(phi_sum,count)==r2*(c-n)+a*n
            assert F(sigma_sum,count)==r3*(c-n)+a*n
            assert F(four_sum,count)==r4*(c-n)+a*n
            if n>=4:
                h4=r4-2*a*r3+a*a*r2
                assert h4==r2*(1-a)*(6*(1-a)-a*n)/((n-2)*(n-3))
    return {"all_interval_subsets":total,"four_ap_free_subsets_including_empty":free,
            "largest_interval":14,"arithmetic":"exact integers and fractions"}


def make_window(p,coordinates):
    points=[]; lifts={}
    for x in range(p):
        row=[]
        for xi,lo,hi in coordinates:
            t=xi*x % p
            t+=((lo-t+p-1)//p)*p
            if t>hi: break
            row.append(t)
        if len(row)==len(coordinates):points.append(x);lifts[x]=row
    return points,lifts


def window_geometry(p,coordinates):
    points,lifts=make_window(p,coordinates)
    pointset=set(points);n=len(points);inv3=pow(3,-1,p)
    labels=[tuple(t%3 for t in lifts[x]) for x in points]
    endpoint=[[int(((2*u+v)*inv3)%p in pointset and ((u+2*v)*inv3)%p in pointset)
               for v in points] for u in points]
    assert all(endpoint[i][j]==int(labels[i]==labels[j]) for i in range(n) for j in range(n))
    completion=[[int((2*y-z)%p in pointset and (2*z-y)%p in pointset)
                 for z in points] for y in points]
    c=sum(map(sum,completion))
    assert c==sum(labels.count(label)**2 for label in set(labels))
    assert c*3**len(coordinates)>=n*n
    return points,lifts,completion,c


def quantile_check(p,coordinates,bits,k,geometry):
    points,lifts,rows,c=geometry
    n,m=len(points),sum(bits);d=len(coordinates)
    bins=[]
    for j in range(d):
        order=sorted(range(n),key=lambda i:lifts[points[i]][j])
        coordinate_bins=[0]*n
        for rank,i in enumerate(order):coordinate_bins[i]=min(k-1,rank*k//n)
        assert max(coordinate_bins.count(b) for b in range(k)) <= ceil(n/k)
        bins.append(coordinate_bins)
    cells={}
    for i in range(n):cells.setdefault(tuple(col[i] for col in bins),[]).append(i)
    positive=sum(max(n*sum(bits[i] for i in cell)-m*len(cell),0) for cell in cells.values())
    for row in rows:
        discrepancy=abs(sum((n*bits[i]-m)*row[i] for i in range(n)))
        assert discrepancy*k<=positive*k+4*d*m*n
    phi=sum(bits[i]*bits[j]*rows[i][j] for i in range(n) for j in range(n))
    assert abs(n*n*phi-m*m*c)*k<=2*m*positive*n*k+8*d*m*m*n*n
    # Every quantile joint cell is exactly a same-frequency interval refinement.
    for cell in cells.values():
        refined=[]
        for j,(xi,_,_) in enumerate(coordinates):
            values=[lifts[points[i]][j] for i in cell]
            refined.append((xi,min(values),max(values)))
        refined_points,_=make_window(p,refined)
        assert set(refined_points)=={points[i] for i in cell}


def controlled_windows():
    p=101;coords=[(1,0,32),(13,0,32)]
    geometry=window_geometry(p,coords)
    assert len(geometry[0])==12
    tested=0
    for bits in product((0,1),repeat=12):
        quantile_check(p,coords,bits,3,geometry);tested+=1
    rng=Random(1422026)
    random_cases=0
    for _ in range(500):
        p=rng.choice((31,61,101))
        d=rng.choice((1,2,3))
        coords=[]
        for j in range(d):
            xi=rng.randrange(1,p);lo=rng.randrange(-p//2,p//2)
            width=rng.randrange(1,(p-1)//3+1)
            coords.append((xi,lo,lo+width-1))
        geom=window_geometry(p,coords)
        n=len(geom[0])
        if n<2:continue
        bits=[rng.randrange(2) for _ in range(n)]
        quantile_check(p,coords,bits,min(n,rng.choice((2,3,4))),geom)
        random_cases+=1
    return {"rank_two_exhaustive_subsets":tested,"seeded_extra_windows":random_cases,
            "rank_two_window_points":geometry[0],"rank_two_count_numerator":geometry[3]}


def chirps(values):
    p=len(values)
    phases=[complex(cos(-2*pi*k/p),sin(-2*pi*k/p)) for k in range(p)]
    return {(a,r):sum(values[x]*phases[(a*x*x+r*x)%p] for x in range(p))/p
            for a in range(p) for r in range(p)}


def relative_operator_spectrum():
    p=19;points=list(range(5));aset={1,2,3};n=len(points);a=F(len(aset),n);w=F(n,p)
    bits=[int(x in aset) for x in range(p)];W=[int(x in points) for x in range(p)]
    g=[F(bits[x])-a*W[x] for x in range(p)]
    inv3=pow(3,-1,p)
    K=[[bits[(2*u+v)*inv3%p]*bits[(u+2*v)*inv3%p] for v in points] for u in points]
    mixed=sum(g[u]*K[i][j]*g[v] for i,u in enumerate(points) for j,v in enumerate(points))/(p*p)
    assert mixed==F(-12,25*p*p)
    chi=[complex(cos(2*pi*(3*(x-1)*(x-3)%p)/p),sin(2*pi*(3*(x-1)*(x-3)%p)/p)) for x in points]
    ray=sum(chi[i].conjugate()*K[i][j]*chi[j] for i in range(n) for j in range(n))/(p*p)
    expected=(3+4*cos(18*pi/19))/(p*p)
    assert abs(ray-expected)<1e-12 and expected<0
    qb,qg=chirps(bits),chirps([float(x) for x in g])
    alpha=a*w;v=alpha*(1-a)
    S=sum(abs(qg[j,r])**2*abs(qb[3*j%p,3*r%p])**2 for j in range(p) for r in range(p))
    target=alpha*v+mixed-alpha*(1-a)**2/p
    assert abs(S-float(target))<1e-12
    energy=sum(float(x*x) for x in g)/p
    fourth=sum(float(x**4) for x in g)/p
    moment4=sum(abs(z)**4 for z in qg.values())
    assert abs(moment4-(2*energy**2-fourth/p))<1e-12
    # A different window shows local generic-negative-spectrum claims fail.
    points2=list(range(6));aset2={0,3}
    K2=[[int((2*u+v)*inv3%p in aset2 and (u+2*v)*inv3%p in aset2) for v in points2] for u in points2]
    assert all(K2[i][j]==int(i==j and points2[i] in aset2) for i in range(6) for j in range(6))
    return {"p":p,"window":points,"A":sorted(aset),"mixed":str(mixed),
            "negative_quadratic_rayleigh":expected,"all_chirp_identity_residual":abs(S-float(target)),
            "floating_tolerance":1e-12,"PSD_local_counterexample":{"window":points2,"A":sorted(aset2)}}


def interval_large_checks():
    results=[]
    for n,period in ((8192,2),(16384,4),(32768,8),(65536,16)):
        bits=[int(i%period==0) for i in range(n)]
        phi,sigma,four,disc=interval_counts(bits)
        m=sum(bits);a=F(m,n);c=(n*n+2)//3
        k=4096;tau=F(1,256)
        sizes=[];masses=[]
        for j in range(k):
            lo=j*n//k;hi=(j+1)*n//k
            sizes.append(hi-lo);masses.append(sum(bits[lo:hi]))
        no_gain=all(F(x,l)<=a*(1+tau) for x,l in zip(masses,sizes))
        if no_gain:
            assert abs(F(phi)-a*a*c)<a*a*c/16
        results.append({"length":n,"density":str(a),"no_coarse_gain":no_gain,
                        "relative_phi_error":str(abs(F(phi)-a*a*c)/(a*a*c)),
                        "AP_free":four==m})
    # The actual interval theorem constants and high-signal prime-first margin.
    error=12*F(1,256)+24*(1+F(1,256))/4096
    assert error<F(1,16)
    assert F(17997,24000)>F(2319,3100)
    return results


def main():
    results={"status":"relative-window diagnostics passed; ultimate r4 target not proved",
             "intervals":interval_exhaustive(),"controlled_windows":controlled_windows(),
             "relative_operator":relative_operator_spectrum(),"large_interval_stability":interval_large_checks(),
             "external_dependencies":[]}
    print(json.dumps(results,indent=2))


if __name__=="__main__":main()
