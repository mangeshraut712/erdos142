"""Independent finite audit of arithmetic pair near-positivity and cell tradeoff.

Exact rational physical counts are distinct from floating Fourier/operator checks.
Synthetic trajectories verify only a conditional ledger, not spectral existence.
Writes WEIGHTED_PAIR_VERIFICATION_20261016.json; no historical file is changed.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import math
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
counts=Counter();errors=Counter();rng=np.random.default_rng(1421616)
PAIRS=list(combinations(range(4),2))


def close(label,x,y,tol=2e-10):
    err=float(np.max(np.abs(np.asarray(x)-np.asarray(y))))
    errors[label]=max(errors[label],err)
    assert err<tol,(label,err)
    counts[label]+=1


def fi(t,p,H):
    return max(0,H+1-min(t%p,(-t)%p))


def weight(x,h,p,H,lin,quad):
    return math.prod(fi(xi*h,p,H) for xi in lin)*math.prod(
        fi((2*c*x+b)*h,p,H)*fi(c*h*h,p,H) for c,b in quad)


def distribution(p,H,lin,quad):
    ft=np.fft.fft([fi(t,p,H)/(H+1) for t in range(p)])/p
    assert max(abs(ft.imag))<1e-13 and min(ft.real)>-1e-13
    ft=ft.real;dist=defaultdict(float);d=len(lin);s=len(quad)
    for ix in product(range(p),repeat=d+2*s):
        ls=ix[:d];ms=ix[d:d+s];ns=ix[d+s:]
        C=sum(c*t for (c,b),t in zip(quad,ms))%p
        beta=(sum(xi*t for xi,t in zip(lin,ls))+sum(b*t for (c,b),t in zip(quad,ms)))%p
        N=sum(c*t for (c,b),t in zip(quad,ns))%p
        dist[C,beta,N]+=math.prod(ft[t] for t in ix)
    close('floating_frequency_probability_mass',sum(dist.values()),1)
    return dist


# Exact modular frequency identity, including all diagonal input pairs.
for p in [5,7,11,13]:
    params=list(product(range(p),repeat=3)) if p<=7 else [tuple(map(int,rng.integers(0,p,3))) for _ in range(35)]
    v=np.arange(p,dtype=np.int64)[:,None];z=np.arange(p,dtype=np.int64)[None,:]
    for i,j in PAIRS:
        invD=pow(j-i,-1,p);h=((z-v)*invD)%p;x=((j*v-i*z)*invD)%p
        for C,beta,N in params:
            direct=(2*C*x*h+N*h*h+beta*h)%p
            expanded=((N-2*j*C)*v*v+(N-2*i*C)*z*z+2*((i+j)*C-N)*v*z)*invD**2+beta*(z-v)*invD
            assert np.array_equal(direct,expanded%p)
            if N==((i+j)*C)%p:
                q=lambda y:(C*invD*y*y+beta*invD*y)%p
                assert np.array_equal(direct,(q(z)-q(v))%p)
                counts['exact_separable_frequency_identity']+=1
            counts['exact_pair_frequency_identity']+=1

# Nonseparable normalized transform norm, independently via singular values.
for p in [5,7,11,17]:
    v=np.arange(p)[:,None];z=np.arange(p)[None,:]
    for sigma in [1,2,p-1]:
        A,B,alpha,beta=map(int,rng.integers(0,p,4))
        K=np.exp(2j*np.pi*((A*v*v+sigma*v*z+B*z*z+alpha*v+beta*z)%p)/p)/p
        close('floating_nonseparable_singular_values',np.linalg.svd(K,compute_uv=False),np.ones(p)/math.sqrt(p))
        close('floating_nonseparable_operator_Gram',K@K.conj().T,np.eye(p)/p)


spectral_records=[]
configs=[(7,1,[1],[]),(7,1,[1,2],[]),(7,1,[],[(1,0)]),
         (11,2,[1],[(2,3)]),(11,1,[],[(1,0),(2,1)]),
         (7,1,[],[(1,1),(1,1)]),(13,2,[1,1],[(1,2)]),
         (17,4,[],[(3,1)]),(53,26,[],[(1,0)])]
negative_vector=[0,8,3,-16,0,2,9,-3,-8,-2,0,9,-9,5,0,-15,16,6,0,-5,-6,-9,40,-8,-40,8,
                 15,15,8,-40,-8,40,-9,-6,-5,0,6,16,-15,0,5,-9,9,0,-2,-8,-3,9,2,0,-16,3,8]
for p,H,lin,quad in configs:
    assert 2*H<p
    den=(H+1)**(len(lin)+2*len(quad))
    W=np.array([[weight(x,h,p,H,lin,quad) for h in range(p)] for x in range(p)],dtype=np.int64)
    F=W/den;dist=distribution(p,H,lin,quad)
    x=np.arange(p)[:,None];h=np.arange(p)[None,:]
    reconstructed=np.zeros((p,p),complex)
    for (C,beta,N),prob in dist.items():
        reconstructed+=prob*np.exp(2j*np.pi*((2*C*x*h+N*h*h+beta*h)%p)/p)
    close('floating_weight_reconstruction',reconstructed,F)
    fields=[np.ones(p),np.eye(1,p,0).ravel(),np.array([(v%5)-2 for v in range(p)],float),
            np.cos(2*np.pi*np.arange(p)/p),np.cos(2*np.pi*(np.arange(p)**2%p)/p)]
    for _ in range(3):
        A=set(rng.choice(p,size=max(1,p//4),replace=False).tolist())
        B=np.array([int(v in A) for v in range(p)],float)
        fields.append(B-B.mean())
    if p==53:fields.append(np.array(negative_vector,float))
    qtable=np.exp(-2j*np.pi*((np.arange(p)[:,None,None]*np.arange(p)[None,None,:]**2+
                            np.arange(p)[None,:,None]*np.arange(p)[None,None,:])%p)/p)
    transformed=[np.einsum('ctx,x->ct',qtable,u)/p for u in fields]
    pair_records=[]
    for i,j in PAIRS:
        D=j-i;invD=pow(D,-1,p)
        vv=np.arange(p)[:,None];zz=np.arange(p)[None,:]
        xx=((j*vv-i*zz)*invD)%p;hh=((zz-vv)*invD)%p
        matrix=F[xx,hh]/p
        sym=(matrix+matrix.T)/2
        positive=np.zeros((p,p),complex);nu=0.
        for (C,beta,N),prob in dist.items():
            if N!=((i+j)*C)%p:continue
            nu+=prob
            phase=np.exp(-2j*np.pi*((C*invD*np.arange(p)**2+beta*invD*np.arange(p))%p)/p)
            positive+=prob*np.outer(phase,phase.conj())/p
        close('floating_pair_kernel_trace',np.trace(sym),1)
        close('floating_positive_kernel_trace',np.trace(positive),nu)
        assert np.linalg.eigvalsh(positive).min()>-2e-10
        norm=float(np.max(abs(np.linalg.eigvalsh(sym-positive))))
        assert norm<=(1-nu)/math.sqrt(p)+2e-10,(p,i,j,norm,nu)
        counts['floating_pair_operator_near_PSD']+=1
        vals=[]
        for u,Q_u in zip(fields,transformed):
            U=float(np.mean(u*u))
            J=float(np.mean(F*u[(x+i*h)%p]*u[(x+j*h)%p]))
            Z=sum(prob*abs(Q_u[C*invD%p,beta*invD%p])**2
                  for (C,beta,N),prob in dist.items() if N==((i+j)*C)%p)
            close('floating_pair_square_vs_operator',Z,np.vdot(u,positive@u)/p)
            assert Z>=-1e-12
            assert abs(J-Z)<=(1-nu)*U/math.sqrt(p)+2e-9
            counts['floating_pair_square_and_error_bound']+=1
            vals.append({'J':J,'Z':float(Z),'U':U,'error_bound':(1-nu)*U/math.sqrt(p)})
        pair_records.append({'slots':[i,j],'nu':float(nu),'operator_error_norm':norm,'fields':vals})
    spectral_records.append({'p':p,'H':H,'linear':lin,'quadratic':quad,
                             'mu':dist.get((0,0,0),0.),'pairs':pair_records})
    if p==53:
        raw=sum(weight(x,h,p,H,lin,quad)*sum(negative_vector[(x+i*h)%p]*negative_vector[(x+j*h)%p]
                                            for i,j in PAIRS) for x in range(p) for h in range(p))
        assert Q(raw,p*p*den)==Q(-8242732,2047761)
        U=Q(sum(v*v for v in negative_vector),p)
        new_lower=-sum(1-z['nu'] for z in pair_records)*float(U)/math.sqrt(p)
        assert float(Q(raw,p*p*den))>=new_lower-1e-10
        counts['exact_old_negative_arithmetic_witness']+=1
        counts['floating_old_witness_new_lower_bound']+=1


# Read saved finite examples as data, then independently recount all terms.
old=json.loads((ROOT/'verification'/'results'/'LOG_DENSITY_VERIFICATION_20261016.json').read_text())
proper_records=[]
for case in old['weighted_host_cases']:
    p=case['p'];H=case['H'];linear=case['linear'];quadratic=case['quad']
    lin=[v[0] for v in linear];quad=[(q[0],q[1]) for q in quadratic]
    den=(H+1)**(len(lin)+2*len(quad))
    def inside(v,erosion):
        return all(erosion<=(xi*v-start)%p<length-erosion for xi,start,length in linear) and all(
            erosion<=(c*v*v+b*v+e-start)%p<length-erosion for c,b,e,start,length in quadratic)
    Om={v for v in range(p) if inside(v,0)};interior={v for v in Om if inside(v,12*H)}
    n=len(Om);w=Q(n,p);bdry=Q(n-len(interior),p);mu=Q(case['mu'])
    assert n==case['n']
    terms=[]
    for x in range(p):
        for h in range(p):
            z=weight(x,h,p,H,lin,quad)
            if z:
                vertices=[(x+j*h)%p for j in range(4)]
                terms.append((h,vertices,z))
    ex_records=[]
    for example in case['examples']:
        A=set(example['A']);a=Q(len(A),n)
        assert not any((2*y-x)%p in A and (3*y-2*x)%p in A for x in A for y in A if x!=y)
        un=[n*int(v in A)-len(A)*int(v in Om) for v in range(p)]
        U=Q(sum(v*v for v in un),p*n*n)
        assert U==w*a*(1-a)
        counts['exact_Boolean_relative_variance']+=1
        full=[0]*6;restricted=[0]*6;diag=[0]*6;absolute_missing=[0]*6
        for h,vertices,z in terms:
            all_inside=all(v in Om for v in vertices)
            for q,(i,j) in enumerate(PAIRS):
                val=z*un[vertices[i]]*un[vertices[j]]
                full[q]+=val
                if h==0:diag[q]+=val
                if all_inside:restricted[q]+=val
                else:
                    absolute_missing[q]+=abs(val)
                    if val:
                        assert vertices[i] in Om-interior and vertices[j] in Om-interior
        beta_boundary=(float(mu)+1/math.sqrt(p))*float(bdry)+1/p
        for q in range(6):
            J=Q(full[q],p*p*den*n*n);JO=Q(restricted[q],p*p*den*n*n)
            assert Q(diag[q],p*p*den*n*n)==U/p
            assert abs(JO-J)<=Q(absolute_missing[q],p*p*den*n*n)
            assert float(Q(absolute_missing[q],p*p*den*n*n))<=beta_boundary+1e-12
            assert float(J)>=-float(U)/math.sqrt(p)-1e-12
            counts['exact_full_and_restricted_pair_diagonal']+=1
            counts['floating_pair_boundary_error']+=1
            counts['floating_rational_pair_lower_bound']+=1
        R2=a*a*sum(Q(z,p*p*den*n*n) for z in restricted)
        assert R2==Q(example['coefficients'][2])
        assert sum(Q(diag[q],p*p*den*n*n) for q in range(6))*a*a==6*a*a*U/p
        bound=6*float(a*a)*(beta_boundary+float(U)/math.sqrt(p))
        assert float(R2)>=-bound-1e-12
        counts['exact_R2_expansion_and_diagonal']+=1
        counts['floating_proper_window_R2_lower_bound']+=1
        ex_records.append({'A':sorted(A),'density':str(a),'U':str(U),'R2':str(R2),'lower_bound':-bound})
    proper_records.append({'p':p,'H':H,'n':n,'boundary':str(bdry),'mu':str(mu),'examples':ex_records})


# Exhaust all feasible cell count triples at small sizes. They are genuine
# Boolean incidence statistics; no AP-free property is needed for this lemma.
small_gain=large_gain=0
for n in range(2,26):
    for occupied in range(1,n):
        a=Q(occupied,n)
        for cellsize in range(1,n):
            muc=Q(cellsize,n)
            for cell_occupied in range(max(0,occupied+cellsize-n),min(occupied,cellsize)+1):
                aprime=Q(cell_occupied,cellsize)
                if aprime<=a:continue
                m=Q(cell_occupied,n)-a*muc;gamma=aprime/a-1
                eta=min(Q(1,4),m/a)
                assert muc*gamma==m/a and muc*gamma>=eta
                assert muc>=a*eta/(1-a)
                cost=math.log(1/float(muc));lg=math.log(float(aprime/a))
                if gamma<=1:
                    assert cost<=2*lg/(math.e*float(eta))+1e-12
                    small_gain+=1
                else:
                    assert cost<=math.log(1/float(a*eta))+1e-12
                    large_gain+=1
                counts['exact_cell_gain_mass_tradeoff']+=1
                counts['floating_cell_size_loss_bound']+=1
assert small_gain and large_gain

# Synthetic trajectories: feasible cell probability statistics, not AP-free sets.
trajectory_records=[]
for initial in [1e-2,1e-3,1e-4]:
    for mode in ['moderate','large','mixed']:
        C=.03;a=initial;loss=0.;steps=0;epochs=defaultdict(lambda:{'steps':0,'small_log_gain':0.,'big_steps':0,'loss':0.})
        while a<=.8:
            R=math.log(math.log(math.e**2/a));eta=C*math.sqrt(a)*R
            choice=1/math.e if mode=='moderate' else eta/2
            if mode=='mixed':choice=[1/math.e,.9,eta/2][steps%3]
            muc=max(choice,2*a*eta/(1-a))
            assert 0<muc<1-eta
            gamma=eta/muc;aprime=a*(1+gamma)
            assert 0<aprime<1
            outside=a*(1-muc-eta)/(1-muc)
            assert 0<=outside<=1
            assert abs(muc*aprime+(1-muc)*outside-a)<1e-12
            jj=int(math.floor(math.log(a/initial,2)+1e-12))
            e_j=initial*2**jj
            if e_j>.8:jj-=1;e_j/=2
            rec=epochs[jj];rec['steps']+=1;rec['loss']+=math.log(1/muc)
            if gamma<=1:rec['small_log_gain']+=math.log1p(gamma)
            else:rec['big_steps']+=1
            loss+=math.log(1/muc);steps+=1;a=aprime
            assert steps<100000
        Dbound=0;Sbound=0;ej=initial
        while ej<=.8:
            upper=min(2*ej,.8)
            lower=C*math.sqrt(ej)*math.log(math.log(math.e**2/upper))
            Bj=1+math.ceil(2*math.log(2)/lower)
            size=4*math.log(2)/(math.e*lower)+math.log(1/(ej*lower))
            jj=int(round(math.log(ej/initial,2)))
            rec=epochs[jj]
            assert rec['steps']<=Bj
            assert rec['small_log_gain']<=math.log(4)+1e-10
            assert rec['big_steps']<=1
            assert rec['loss']<=size+1e-10
            Dbound+=Bj;Sbound+=size;ej*=2
        assert steps<=Dbound and loss<=Sbound+1e-9
        counts['floating_complete_conditional_trajectory']+=1
        trajectory_records.append({'initial_density':initial,'mode':mode,'steps':steps,'log_size_loss':loss,
                                   'rank_bound':Dbound,'size_loss_bound':Sbound,'terminal_density':a,
                                   'actual_APfree_trajectory':False})

def u3_eighth(f):
    p=len(f)
    return float(sum(np.sum(abs(np.fft.fft(f*np.conj(np.roll(f,-h)))/p)**4)
                     for h in range(p))/p)


# Fractional real quadratic on integer lifts; global finite-field chirps only.
chirp_records=[]
for p in [17,31,53,101,257,1009]:
    L=p//8;x=np.arange(p);P=(x<=L).astype(float);w=float(P.mean())
    f=P*np.exp(2j*np.pi*math.sqrt(p)*x*x/(p*p))
    fhat=np.fft.fft(f)/p
    diff=float(np.mean(abs(np.roll(f,-1)-f)**2))
    assert diff<=(2+math.pi**2/8)/p+1e-12
    tilde=np.minimum(x,p-x)
    assert np.sum(tilde**2*abs(fhat)**2)<=(2+math.pi**2/8)*p/16+1e-10
    assert np.sum((1+tilde**2/p)*abs(fhat)**2)<=1+1e-12
    assert np.sum(abs(fhat))<=math.sqrt(math.pi+1)*p**.25+1e-12
    counts['floating_fractional_chirp_Sobolev_bound']+=1
    phase=np.exp(-2j*np.pi*((x[:,None]*x[None,:]**2)%p)/p)
    all_Q=np.fft.fft(phase*f[None,:],axis=1)/p
    linear=float(max(abs(all_Q[0])))
    nonlinear=float(np.max(abs(all_Q[1:])))
    assert linear**2<=1/p+(1+math.log(p))/(2*math.sqrt(p))+1e-12
    assert nonlinear<=np.sum(abs(fhat))/math.sqrt(p)+1e-12
    Dp=3*p**(-.25)*math.sqrt(1+math.log(p))
    assert max(linear,nonlinear)<=Dp+1e-12
    counts['floating_complete_global_chirp_grids']+=1
    f8=u3_eighth(f);P8=u3_eighth(P)
    close('floating_fractional_chirp_cube_identity',f8,P8)
    assert f8>=32**(-4)-1e-12
    if p<=53:
        cube_count=0
        for base in range(L+1):
            for axes in product(range(L+1),repeat=3):
                hs=[v-base for v in axes]
                vertices=[(base+sum(hs[i]*bits[i] for i in range(3)))%p
                          for bits in product([0,1],repeat=3)]
                if max(vertices)>L:continue
                cube_count+=1
                alternating=sum((-1)**sum(bits)*v*v for bits,v in zip(product([0,1],repeat=3),vertices))
                assert alternating==0
                counts['exact_integer_lift_cube_phase_cancellation']+=1
        close('floating_cube_vs_exact_count',f8,float(Q(cube_count,p**4)))
        assert cube_count>=(p//32+1)**4
        counts['exact_fractional_chirp_cube_lower_bound']+=1
    realnorm=u3_eighth(f.real)**.125;imagnorm=u3_eighth(f.imag)**.125
    assert max(realnorm,imagnorm)>=f8**.125/2-1e-11
    h=f.real if realnorm>=imagnorm else f.imag
    m=float(np.sum(h)/np.sum(P));v=(h-m*P)/2
    close('floating_real_residual_relative_mean',float(np.sum(v)/np.sum(P)),0)
    assert max(abs(v))<=1+1e-12
    Qv=np.fft.fft(phase*v[None,:],axis=1)/p
    actual_cap=max(linear,nonlinear)
    assert np.max(abs(Qv))<=actual_cap+1e-12
    normv=u3_eighth(v)**.125
    assert normv>=1/(4*math.sqrt(32))-Dp/(2*w)-1e-10
    counts['floating_real_centered_chirp_obstruction']+=1
    a=1/math.log(p);B_weight=a*(P+v)
    assert min(B_weight)>=-1e-12 and max(B_weight)<=1+1e-12
    close('floating_log_density_weight_mean',float(B_weight.sum()/P.sum()),a)
    if L>=3:
        assert np.prod(B_weight[:4])>0
        counts['floating_weight_has_actual_progression']+=1
    chirp_records.append({'p':p,'window_size':L+1,'U3_f':f8**.125,'U3_real_centered':normv,
                          'max_global_linear':linear,'max_global_quadratic_nonzero_slope':nonlinear,
                          'max_global_chirp_centered_real':float(np.max(abs(Qv))),
                          'all_chirps_checked':p*p,'theoretical_Dp':Dp,
                          'Boolean':False,'support_contains_four_consecutive':L>=3,
                          'AP_free_counterexample_claimed':False})

out={'date':'2026-10-16','cycle':'weighted pair reduction and direct increment tradeoff',
     'offline':True,'target_proved':False,'counts':dict(counts),
     'max_floating_identity_errors':dict(errors),'spectral_cases':spectral_records,
     'proper_window_cases':proper_records,'cell_cases':{'small_gain':small_gain,'large_gain':large_gain},
     'conditional_trajectories':trajectory_records,
     'global_chirp_obstruction_cases':chirp_records,
     'global_chirp_coefficients_examined':sum(z['all_chirps_checked'] for z in chirp_records),
     'scope':['Near-positivity is proved in the note; these are finite checks.',
              'Generic PSD is still false; the p=53 witness survives the sharper error bound.',
              'No synthetic trajectory asserts phase selection or constructs an AP-free iteration.',
              'DIRECT-Q-GAIN and signed cubic-plus-quartic closure remain open.']}
sources=['docs/audits/WEIGHTED_PAIR_REDUCTION_20261016.md','docs/audits/DIRECT_INCREMENT_TRADEOFF_20261016.md',
         'docs/audits/GLOBAL_CHIRP_INVERSE_OBSTRUCTION_20261016.md',
         'verification/scripts/' + Path(__file__).name,'verification/results/LOG_DENSITY_VERIFICATION_20261016.json']
out['source_sha256']={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in sources}
(ROOT/'verification'/'results'/'WEIGHTED_PAIR_VERIFICATION_20261016.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'counts':dict(counts),'total':sum(counts.values()),'max_errors':dict(errors)},indent=2))
