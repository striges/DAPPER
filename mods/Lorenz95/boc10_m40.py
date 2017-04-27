# Same as boc10, except that here ndim=40 (i.e. Fig. 5 of paper)
from mods.Lorenz95.boc10 import *

m = 40
f['m'] = m
X0 = GaussRV(m=m, C=0.001)

jj = arange(0,m,2)
p  = len(jj)
H  = direct_obs_matrix(m,jj)
@ens_compatible
def partial_direct_obs    (x,t): return x[jj]
def partial_direct_obs_jac(x,t): return H
h = {
    'm'    : p,
    'model': partial_direct_obs,
    'jacob': partial_direct_obs_jac,
    'noise': 1.5,
    'plot' : lambda y: plt.plot(jj,y,'g*',ms=8)[0]
    }
 
other = {'name': os.path.relpath(__file__,'mods/')}

setup = OSSE(f,h,t,X0,**other)

####################
# Suggested tuning
####################
#                                                          # rmse_a 
#cfgs.add(EnKF_N,N=24,rot=True,infl=1.01)                  # 0.38

# NB: Particle filter scores very sensitive to rare events => Need T>=2000.
#cfgs.add(PartFilt,N=3000,NER=0.20,reg=1.2)                # 0.77
#cfgs.add(PartFilt,N=5000,NER=0.10,reg=1.1)                # 0.72
#cfgs.add(PartFilt,N=10000,NER=0.05,reg=0.8)               # 0.45

#cfgs.add(PFD,     N=100, xN=1000,NER=0.9,reg=0.7,Qs=1.0)  # 0.87
#cfgs.add(PFD,     N=100, xN=1000,NER=0.3,reg=0.7,Qs=0.9)  # 0.72 Diverges
#cfgs.add(PFD,     N=1000,xN=100, NER=0.9,reg=0.5,Qs=0.6)  # 0.51
