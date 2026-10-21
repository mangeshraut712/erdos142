"""Supporting finite algebra for PD2--PD7, not a proof of qualitative Szemeredi."""
import json
import math
from fractions import Fraction as F
from pathlib import Path


def run():
    exact = numeric = 0
    maximum_slack_ratio = 0.0
    parameter_cases = []

    # The envelope substitution is homogeneous in rho,e,d0 and f0.
    # Use rational parameters to check all m/R/a coefficients exactly.
    for m in (4, 5, 8, 12, 17):
        for R in range(1, m):
            for a0 in (F(1, 20), F(1, 5), F(1, 2)):
                for a in (a0, (a0+F(4, 5))/2, F(4, 5)):
                    for rho, e, d0, f0 in ((F(1, 10),F(1, 20),F(1, 100),F(1, 100)),
                                          (F(1, 2),F(1, 2),F(1, 5),F(1, 5)),
                                          (F(0),F(0),F(0),F(0)),
                                          (F(1, 1000),F(1, 1000),F(1, 1000),F(1, 1000))):
                        choose=m*(m-1)//2
                        E1=4*m*(rho+e*(1+rho)+2*d0)
                        E2=4*choose*((1+e)*rho+d0+e)
                        exact_expression=(2*abs(F(R-1,2)-(m-1)*a)*E1/(m*(m-1)*a)
                                          +F(m-R,m-1)*4*f0+2*E2/(m*(m-1)*a))
                        tightened=16/a0*(rho+(1+rho)*e)+28/a0*d0+4*f0
                        displayed=32/a0*(rho+(1+rho)*e+d0)+4*f0
                        assert exact_expression <= tightened <= displayed
                        exact += 1
    # Exact consequence of k<=2r and 4log(1/a0)<=log L: write
    # T=r(S+log48r+logL)<=L/100 and Z=r logL<=T.
    for L in (F(100),F(1000),F(100000)):
        for t_frac in (F(1,1000),F(1,200),F(1,100)):
            T=L*t_frac
            for z_frac in (F(1,10),F(1,2),F(1)):
                Z=T*z_frac
                for c_frac in (F(0),F(1,2),F(1)):
                    four_r_log_inv_a0=Z*c_frac
                    assert 2*T+four_r_log_inv_a0 <= F(3,100)*L
                    exact += 1
    assert F(1,2)-F(3,100)==F(47,100)
    assert 1-F(1,100)-F(3,100)==F(96,100)
    assert 1-F(3,100)==F(97,100)
    exact += 3

    # Log-space checks avoid constructing primes of enormous size. These
    # are parameter envelope diagnostics, not actual finite-field hosts.
    for a0 in (0.01,0.1,0.5):
        L=max(10000.0,a0**(-4)*1.01)
        for r in (1, max(1,int(L/(800*math.log(L))))):
            S=max(0.0,L/(200*r)-math.log(48*r)-math.log(L))
            budget=r*(S+math.log(48*r)+math.log(L))
            if budget>L/100:
                continue
            for k in (r,2*r):
                log_inv_mu=k*(S+math.log(48*r)+math.log(L)+2*math.log(1/a0))
                assert log_inv_mu<=0.03*L+1e-10
                assert S<=0.01*L+1e-10
                assert r<=L/(100*math.log(L))+1e-10
                numeric+=3
                maximum_slack_ratio=max(maximum_slack_ratio,log_inv_mu/L)
                parameter_cases.append({'a0':a0,'log_p':L,'r':r,'k':k,
                                        'S':S,'T5_budget_over_log_p':budget/L,
                                        'log_inverse_mu0_over_log_p':log_inv_mu/L,
                                        'scope':'log-space parameter check, not an actual finite-field instance'})
    # Classical finite-pattern conclusion: R/m<a0/4 suffices to get
    # (R-1)/(m-1)<a0/3; no value of r4(m) is asserted by this loop.
    for m in range(4,301):
        for R in range(1,m):
            for a0 in (F(1,5),F(1,2),F(4,5)):
                if F(R,m)<a0/4:
                    assert F(R-1,m-1)<a0/3
                    exact+=1
    return {'status':'passed; finite envelope algebra only',
            'checks':exact+numeric,'exact_rational_checks':exact,
            'floating_log_parameter_checks':numeric,
            'maximum_log_inverse_mu0_over_log_p':maximum_slack_ratio,
            'parameter_cases':parameter_cases,
            'classical_qualitative_theorem_proved_by_script':False,
            'P12_or_target_proved':False,
            'scope':'Supports PD2--PD7; PD8 is an explicitly invoked established theorem; no actual eligible example claimed'}


if __name__=='__main__':
    output=json.dumps(run(),indent=2)+'\n'
    (Path(__file__).resolve().parents[1] / 'results' / 'POSITIVE_DENSITY_BRANCH_VERIFICATION_20261019.json').write_text(output)
    print(output,end='')
