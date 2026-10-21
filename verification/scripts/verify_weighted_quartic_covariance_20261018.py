"""Independent exact geometry and floating weighted-chirp identities.
No asymptotic selection claim; all source/output paths are local to this file.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
counts=Counter(); errors=defaultdict(float)
rng=np.random.default_rng(1421810)

def close(label,x,y,tol=3e-10):
    err=float(np.max(np.abs(np.asarray(x)-np.asarray(y))))
    errors[label]=max(errors[label],err)
    assert err<tol,(label,err)
    counts[label]+=1

def tent(p,H):
    t=np.arange(p)
    return np.maximum(0,H+1-np.minimum(t,p-t))/(H+1)

def distribution(p,H,lin,quad):
    ft=np.fft.fft(tent(p,H))/p
    close('floating_tent_real_nonnegative',ft.imag,0)
    assert min(ft.real)>-1e-12
    dist=defaultdict(float)
    for ix in product(range(p),repeat=len(lin)+2*len(quad)):
        ls=ix[:len(lin)];ms=ix[len(lin):len(lin)+len(quad)];ns=ix[len(lin)+len(quad):]
        C=sum(c*t for (c,b),t in zip(quad,ms))%p
        beta=(sum(z*t for z,t in zip(lin,ls))+sum(b*t for (c,b),t in zip(quad,ms)))%p
        N=sum(c*t for (c,b),t in zip(quad,ns))%p
        dist[C,beta,N]+=float(np.prod([ft[t].real for t in ix]))
    close('floating_probability_mass',sum(dist.values()),1)
    return dist

# Exact modular branch factorization, not inferred from Fourier numerics.
for p in [5,7,11,13]:
    for x0,x1,x2 in product(range(p),repeat=3):
        x3=(x0-3*x1+3*x2)%p
        constraints=(-x0*x0+3*x1*x1-3*x2*x2+x3*x3)%p==0
        AP=(x2==(2*x1-x0)%p and x3==(3*x1-2*x0)%p)
        pairing=(x0==x3 and x1==x2)
        assert constraints==(AP or pairing)
        if AP and pairing: assert x0==x1==x2==x3
        counts['exact_chirp_orthogonality_branches']+=1
    for C,beta,N in product(range(p),repeat=3):
        half=pow(2,-1,p);s=(N-3*C)*half%p;gamma=(N-5*C)*half%p
        gs=[0,gamma,(4*C-N)%p,s];ts=[0,-beta,beta,0]
        assert sum(gs)%p==0 and sum(j*g for j,g in enumerate(gs))%p==C
        assert sum(j*j*g for j,g in enumerate(gs))%p==N
        assert sum(ts)%p==0 and sum(j*t for j,t in enumerate(ts))%p==beta
        counts['exact_mode_phase_absorption']+=1

records=[]
configs=[(5,1,[1],[]),(7,2,[],[(1,0)]),(11,2,[1],[(2,3)]),
         (7,1,[],[(1,1),(1,1)]),(13,3,[],[(2,1)]),(17,2,[1,2],[])]
for p,H,lin,quad in configs:
    y=np.arange(p);x=y[:,None];h=y[None,:]
    slots=[(x+j*h)%p for j in range(4)]
    f=tent(p,H);F=np.ones((p,p))
    for z in lin:F*=f[(z*h)%p]
    for c,b in quad:F*=f[((2*c*x+b)*h)%p]*f[(c*h*h)%p]
    dist=distribution(p,H,lin,quad)
    chirps=np.exp(-2j*np.pi*((y[:,None,None]*y[None,None,:]**2+y[None,:,None]*y[None,None,:])%p)/p)
    P=(y<=3*p//4)
    A=P & (rng.random(p)<.45)
    a=Fraction(int(sum(A)),int(sum(P)))
    fields=[('constant',np.ones(p)),('point',np.eye(1,p,0).ravel()),
            ('real',rng.uniform(-1,1,p)),('boolean_residual',A.astype(float)-float(a)*P)]
    for kind,u in fields:
        Q=np.mean(chirps*u[None,None,:],axis=2)
        U=float(np.mean(u*u));m4=float(np.mean(u**4));V=U*U-m4/p
        D=np.empty((p,p,p),complex);ms=[]
        for s in y:
            m_s=np.mean(u*u*np.exp(2j*np.pi*((s*y*y)%p)/p));ms.append(m_s)
            D[s]=Q*np.conjugate(Q[(y+s)%p,:])-m_s/p
            close('floating_centered_row_sum',np.sum(D[s],axis=1),0)
            close('floating_shifted_energy_universal',np.sum(abs(D[s])**2),V)
            if kind=='boolean_residual':
                QP=np.mean(P*np.exp(2j*np.pi*((s*y*y)%p)/p))
                close('floating_Boolean_baseline',m_s,(1-2*float(a))*Q[-s%p,0]+float(a)*(1-float(a))*QP)
        quartic=np.prod([u[v] for v in slots],axis=0)
        R4=float(np.mean(F*quartic));Gamma=0j;energy=0.
        for (C,beta,N),prob in dist.items():
            half=pow(2,-1,p);s=(N-3*C)*half%p;gamma=(N-5*C)*half%p
            shifted=D[s][(3*y+gamma)%p][:,(3*y-beta)%p]
            cov=np.sum(D[s]*np.conjugate(shifted))
            mode=np.exp(2j*np.pi*((2*C*x*h+N*h*h+beta*h)%p)/p)
            physical=np.mean(mode*quartic)
            close('floating_individual_mode_covariance',cov+m4/p,physical)
            Gamma+=prob*cov
            energy+=prob*float(np.sum(abs(D[s]-shifted)**2))
        close('floating_original_weight_covariance',R4,Gamma+m4/p)
        close('floating_nonnegative_defect_energy_identity',R4,U*U-energy/2)
        assert energy>=-1e-10 and energy<=4*V+1e-10
        assert -U*U+2*m4/p-1e-10<=R4<=U*U+1e-10
        counts['floating_defect_bounds']+=1
        if kind=='boolean_residual':
            # Explicit host indicators on each residual term; all h retained.
            R3=0.
            for missing in range(4):
                R3+=float(a)*np.mean(F*P[slots[missing]]*np.prod([u[slots[j]] for j in range(4) if j!=missing],axis=0))
            close('floating_Q_energy_identity',R3+R4,R3+U*U-energy/2)
        records.append({'p':p,'H':H,'linear':lin,'quadratic':quad,'field':kind,
                        'R4':R4,'U2':U*U,'diagonal':m4/p,'defect_energy':energy})

sources=['verification/scripts/verify_weighted_quartic_covariance_20261018.py','docs/audits/WEIGHTED_QUARTIC_COVARIANCE_20261018.md',
         'docs/audits/WEIGHTED_PAIR_REDUCTION_20261016.md','docs/audits/O2_QUANTIFIERS_CUBIC_BOUND_20261017.md']
out={'date':'2026-10-18','offline':True,'target_proved':False,'counts':dict(counts),
     'total_checks':sum(counts.values()),'max_errors':dict(errors),'cases':records,
     'scope':['Modular branch and phase identities checked exactly.',
              'Fourier and weighted covariance identities checked in floating arithmetic.',
              'All finite primes are outside the target product-budget domain.',
              'No sign, phase selection, P12, or asymptotic target is proved computationally.'],
     'source_sha256':{n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in sources}}
(ROOT/'verification'/'results'/'WEIGHTED_QUARTIC_VERIFICATION_20261018.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'counts':dict(counts),'total_checks':sum(counts.values()),'maximum_error':max(errors.values())},indent=2))
