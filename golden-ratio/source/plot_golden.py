"""Explanatory plots only: floating point rendering is not a proof certificate."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from pathlib import Path

root=Path(__file__).resolve().parent
phi=(1+np.sqrt(5))/2
q=1j/phi
center=phi/(1-q)
def S(z,n): return center+q**n*(z-center)
fig=plt.figure(figsize=(14,5),layout='constrained')
ax=fig.add_subplot(131)
R=np.array([0,phi,phi+1j,1j])
for n in range(8):
    r=S(R,n)
    ax.add_patch(Polygon(np.c_[r.real,r.imag],closed=True,fill=False,
                         edgecolor='#959ca6',linewidth=0.9))
t=np.linspace(0,8,1601)
z=center+(1j-center)*np.exp(t*(-np.log(phi)+1j*np.pi/2))
ax.plot(z.real,z.imag,color='#1b7a78',lw=2,label='Logarithmic spiral')
for n in range(8):
    a=1+1j+np.exp(1j*np.linspace(np.pi,1.5*np.pi,101))
    a=S(a,n)
    ax.plot(a.real,a.imag,color='#c2642e',lw=1.2,ls='--',label='Quarter-circle arcs' if n==0 else None)
ax.scatter([center.real],[center.imag],s=18,color='#253447')
ax.set(aspect='equal',xlim=(-.05,phi+.05),ylim=(-.04,1.04),xlabel='x / initial short side',ylabel='y / initial short side',title='Same scaling; different curves')
ax.legend(loc='lower left',fontsize=8,framealpha=.9)

bx=fig.add_subplot(132)
bx.plot(t,np.zeros_like(t),color='#1b7a78',lw=2,label='Exact lifted spiral')
for n in range(8):
    a=S(1+1j+np.exp(1j*np.linspace(np.pi,1.5*np.pi,101)),n)-center
    theta=np.unwrap(np.angle(a))
    # Align each arc with its declared n-th quarter turn.
    theta=theta-theta[0]+n*np.pi/2
    xx=theta/(np.pi/2)
    yy=np.log(np.abs(a)/abs(1j-center))+xx*np.log(phi)
    bx.plot(xx,yy,color='#c2642e',lw=1.2,ls='--',label='Lifted circular arcs' if n==0 else None)
bx.set(xlabel='unwrapped angle / quarter turn',ylabel='log-radius residual (dimensionless)',title='Normalized shape error persists')
bx.grid(alpha=.2);bx.legend(fontsize=8)

cx=fig.add_subplot(133,projection='3d')
rects=[np.array([[-1,-phi,0],[1,-phi,0],[1,phi,0],[-1,phi,0],[-1,-phi,0]]),
       np.array([[0,-1,-phi],[0,1,-phi],[0,1,phi],[0,-1,phi],[0,-1,-phi]]),
       np.array([[-phi,0,-1],[-phi,0,1],[phi,0,1],[phi,0,-1],[-phi,0,-1]])]
for pts,col in zip(rects,['#1b7a78','#c2642e','#6557a6']):
    cx.plot(*pts.T,color=col,lw=2.5)
    cx.scatter(*pts[:-1].T,color=col,s=12)
cx.set(xlabel='x',ylabel='y',zlabel='z',title='Three perpendicular boundaries')
cx.set_box_aspect((1,1,1));cx.view_init(elev=20,azim=35)
cx.set_xticks([-1,0,1]);cx.set_yticks([-1,0,1]);cx.set_zticks([-1,0,1])
fig.suptitle('Golden-ratio geometry: exact formulas, illustrative rendering',fontsize=14)
fig.savefig(root/'golden_geometry.png',dpi=180)
print(root/'golden_geometry.png')
