"""Bounded exact witnesses for the Golden Ratio / AEG integration proposal.

Run: python verify_golden.py > evidence.json
Standard library only. This is an external research checker, not native adva.
Q5(a,b) means a+b*phi with phi^2=phi+1 and the real embedding 1<phi<2.
No floating-point result is used to accept an algebraic identity.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
import json
import math
import resource
import sys
import time

START = time.perf_counter()
MAX_SECONDS = 30
checks = []

def check(name, value):
    if time.perf_counter() - START > MAX_SECONDS:
        raise TimeoutError('30 second verification budget exceeded')
    if not value:
        raise AssertionError(name)
    checks.append(name)

@dataclass(frozen=True)
class Q5:
    a: F = F(0)
    b: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, 'a', F(self.a))
        object.__setattr__(self, 'b', F(self.b))

    def __add__(self, y):
        if not isinstance(y, Q5): y = Q5(y)
        return Q5(self.a+y.a, self.b+y.b)

    __radd__ = __add__

    def __neg__(self): return Q5(-self.a, -self.b)
    def __sub__(self, y): return self + (-y if isinstance(y,Q5) else -Q5(y))
    def __rsub__(self, y): return -self + y

    def __mul__(self, y):
        if not isinstance(y, Q5): y = Q5(y)
        a,b,c,d = self.a,self.b,y.a,y.b
        return Q5(a*c+b*d, a*d+b*c+b*d)

    __rmul__ = __mul__

    def conj(self): return Q5(self.a+self.b, -self.b)
    def norm(self): return self.a*self.a+self.a*self.b-self.b*self.b

    def inverse(self):
        n = self.norm()
        if n == 0: raise ZeroDivisionError('zero has no inverse in Q(sqrt(5))')
        c = self.conj()
        return Q5(c.a/n,c.b/n)

    def __truediv__(self, y):
        return self*(y if isinstance(y,Q5) else Q5(y)).inverse()

    def __pow__(self, n):
        if n < 0: return self.inverse()**(-n)
        out, base = Q5(1), self
        while n:
            if n & 1: out = out*base
            base = base*base
            n >>= 1
        return out

    def sign(self):
        # 2*(a+b*phi) = c+d*sqrt(5); comparison uses rational squares.
        c,d = 2*self.a+self.b,self.b
        sg = lambda x: (x>0)-(x<0)
        if not d: return sg(c)
        if not c or sg(c)==sg(d): return sg(d)
        return sg(c)*sg(c*c-5*d*d)

    def __lt__(self, y): return (self-y).sign()<0
    def __le__(self, y): return (self-y).sign()<=0
    def pair(self): return [str(self.a), str(self.b)]

ZERO, ONE, PHI = Q5(), Q5(1), Q5(0,1)
RHO = PHI-1
check('minimal_polynomial', PHI**2-PHI-1 == ZERO)
check('positive_embedding', Q5(1)<PHI<Q5(2))
check('conjugation_not_inverse', PHI.conj() == -RHO and PHI.conj()!=RHO)
check('norm_phi_minus_one', PHI.norm()==-1)
check('reciprocal_roots', PHI**2 * PHI**-2 == ONE)
check('reciprocal_root_sum', PHI**2 + PHI**-2 == Q5(3))
for a in range(-2,3):
    for b in range(-2,3):
        q=Q5(a,b)
        if q!=ZERO: check(f'inverse_{a}_{b}', q*q.inverse()==ONE)
try:
    ZERO.inverse()
    raise AssertionError('zero accepted')
except ZeroDivisionError:
    check('zero_inverse_rejected',True)
formation_ms=(time.perf_counter()-START)*1000

def compose(f,g): return (f[0]*g[0], f[0]*g[1]+f[1])
def word(t,w):
    ops={'a':(t,ZERO),'A':(t.inverse(),ZERO),'b':(ONE,ONE),'B':(ONE,-ONE)}
    out=(ONE,ZERO)
    for c in w: out=compose(out,ops[c])
    return out
word_cases=[]
for label,t,w,expected in [
    ('root',PHI**2,'abbbaBAAB',(ONE,ZERO)),
    ('conjugate_root',PHI**-2,'abbbaBAAB',(ONE,ZERO)),
    ('wrong_phi_parameter',PHI,'abbbaBAAB',(ONE,2*PHI-2)),
    ('deleted_b',PHI**2,'abbaBAAB',(ONE,-PHI**2))]:
    out=word(t,w)
    check(label,out==expected)
    word_cases.append({'name':label,'parameter':t.pair(),'word':w,'affine':[q.pair() for q in out]})
t=PHI**-2
check('HNN_u', ONE/t == ONE+PHI)
check('HNN_v', PHI/t == ONE+2*PHI)
check('HNN_commuting_shadow',compose((ONE,ONE),(ONE,PHI))==compose((ONE,PHI),(ONE,ONE)))

fib=[0,1]
for _ in range(34): fib.append(sum(fib[-2:]))
for n in range(1,33):
    check(f'power_fib_{n}',PHI**n == Q5(fib[n-1],fib[n]))
    check(f'cassini_{n}',fib[n+1]*fib[n-1]-fib[n]**2 == (-1)**n)
    q=F(fib[n+1],fib[n]);r=F(fib[n+2],fib[n+1]);lo,hi=sorted((q,r))
    check(f'bracket_{n}',Q5(lo)<PHI<Q5(hi) and hi-lo==F(1,fib[n]*fib[n+1]))
ratio=F(1);cf=[ratio]
for _ in range(6): ratio=1+1/ratio;cf.append(ratio)

# The general positive continued-fraction tail has not been silently fixed.
# Six fixed partial quotients have endpoint images F_6/F_5 and F_7/F_6.
check('unknown_tail_not_singleton',F(8,5)!=F(13,8))
check('six_step_seed_certificate', sorted(cf[-2:])==[F(21,13),F(13,8)])
reverse=[F(13,8)]
while reverse[-1]!=1 and len(reverse)<10:
    reverse.append(1/(reverse[-1]-1))
check('rational_reverse_terminates',reverse==[F(13,8),F(8,5),F(5,3),F(3,2),F(2),F(1)])

# Rectangle R=[0,phi]x[0,1]. S(x,y)=(phi-y/phi,x/phi).
def S(p): return (PHI-p[1]/PHI,p[0]/PHI)
def Sinv(p): return (p[1]*PHI,(PHI-p[0])*PHI)
center=(PHI/(1+RHO**2),ONE/(1+RHO**2))
check('rectangle_fixed_point',S(center)==center)
for p in [(ZERO,ZERO),(PHI,ZERO),(PHI,ONE),(ZERO,ONE),center]:
    check('rectangle_inverse_'+str(p),Sinv(S(p))==p)
check('one_step_inside',set(S(p) for p in [(ZERO,ZERO),(PHI,ZERO),(PHI,ONE),(ZERO,ONE)])==set([(ONE,ZERO),(PHI,ZERO),(PHI,ONE),(ONE,ONE)]))
area_sum=ZERO
for n in range(1,17):
    area_sum += RHO**(2*(n-1))
    check(f'coverage_area_{n}',area_sum+PHI*RHO**(2*n)==PHI)
    check(f'positive_residual_{n}',ZERO<PHI*RHO**(2*n))
diameter_sq=(PHI**2+1)*RHO**24
check('twelve_step_diameter_lt_001',diameter_sq<Q5(F(1,10000)))

# Twelve exact vertices. Edge and triangular-face incidence derived independently.
verts=[]
for s in (-1,1):
    for t in (-1,1):
        verts += [(ZERO,Q5(s),t*PHI),(Q5(s),t*PHI,ZERO),(t*PHI,ZERO,Q5(s))]
check('twelve_unique_vertices',len(set(verts))==12)
edges=[]
for i,j in combinations(range(12),2):
    d=sum(((a-b)**2 for a,b in zip(verts[i],verts[j])),ZERO)
    check(f'icosahedron_pair_{i}_{j}',Q5(4)<=d)
    if d==Q5(4):edges.append((i,j))
E=set(edges)
faces=[c for c in combinations(range(12),3) if all(tuple(sorted(e)) in E for e in combinations(c,2))]
check('icosahedron_edges_faces',len(edges)==30 and len(faces)==20)
check('icosahedron_degrees',all(sum(i in e for e in edges)==5 for i in range(12)))
check('unit_area_square_75',Q5(75)!=(10*PHI**2)**2)

# Curvature -1 metric: cosh d(P,Q)=1+|P-Q|^2/(2 Im(P) Im(Q)).
tangent_points=[(F(0),F(1)),(F(1),F(1)),(F(1,2),F(1,2))]
for p,q in combinations(tangent_points,2):
    cosh_d=1+sum((a-b)**2 for a,b in zip(p,q))/(2*p[1]*q[1])
    check('tangency_distance_cosh',cosh_d==F(3,2))
check('cosh_2_log_phi',(PHI**2+PHI**-2)/2==Q5(F(3,2)))
check('trace_three_translation_length',PHI**2+PHI**-2==Q5(3))

# Six parallel rewriting steps, ordered words retained separately from counts.
s='A';substitution=[]
for n in range(1,7):
    s=''.join('AB' if c=='A' else 'A' for c in s)
    check(f'substitution_count_{n}',(s.count('A'),s.count('B'))==(fib[n+1],fib[n]))
    substitution.append(s)

def golden_search(root,steps,reuse):
    """Known strictly convex objective (x-root)^2; fixed field and frame."""
    a,b=ZERO,ONE;calls=0;rows=[]
    def evaluate(x):
        nonlocal calls
        calls+=1
        return (x-root)**2
    x=a+(1-RHO)*(b-a);y=a+RHO*(b-a)
    fx,fy=evaluate(x),evaluate(y)
    for n in range(steps):
        if fx<=fy:
            b=y
            if n+1<steps:
                if reuse:
                    y,fy=x,fx;x=a+(1-RHO)*(b-a);fx=evaluate(x)
                else:
                    x=a+(1-RHO)*(b-a);y=a+RHO*(b-a);fx,fy=evaluate(x),evaluate(y)
        else:
            a=x
            if n+1<steps:
                if reuse:
                    x,fx=y,fy;y=a+RHO*(b-a);fy=evaluate(y)
                else:
                    x=a+(1-RHO)*(b-a);y=a+RHO*(b-a);fx,fy=evaluate(x),evaluate(y)
        check(f'search_coverage_{root.a}_{reuse}_{n}',a<=root<=b and b-a==RHO**(n+1))
        rows.append([a.pair(),b.pair()])
    return {'calls':calls,'intervals':rows}

search=[]
for root in (Q5(F(3,7)),Q5(F(2,3))):
    start=time.perf_counter();base=golden_search(root,12,False);base_ms=(time.perf_counter()-start)*1000
    start=time.perf_counter();reuse=golden_search(root,12,True);reuse_ms=(time.perf_counter()-start)*1000
    check('search_identical_trace_'+str(root.a),base['intervals']==reuse['intervals'])
    check('search_call_saving_'+str(root.a),base['calls']==24 and reuse['calls']==13)
    search.append({'root':root.pair(),'baseline':base,'reuse':reuse,'baseline_ms':base_ms,'reuse_ms':reuse_ms})

validation_ms=(time.perf_counter()-START)*1000
result={
 'status':'passed','scope':'external exact finite checks; no native adva execution',
 'budget':{'seconds':MAX_SECONDS,'max_index':32,'max_search_steps':12,'unknown_tail':'retained'},
 'field':{'polynomial':'u^2-u-1','embedding':'1<u<2','encoding':'rational coefficient pair'},
 'checks':checks,'check_count':len(checks),'word_cases':word_cases,
 'continued_fraction_seed_1_six_steps':list(map(str,cf)),
 'positive_unknown_tail_six_prefix_interval':['8/5','13/8'],
 'rational_reverse':list(map(str,reverse)),
 'rectangle_center':[q.pair() for q in center],
 'rectangle_diameter_squared_after_12':diameter_sq.pair(),
 'icosahedron':{'vertices':12,'edges':len(edges),'faces':len(faces),'unit_edge_area':'5*sqrt(3)','topological_link_certificate':'not constructed'},
 'hyperbolic':{'curvature':-1,'tangency_side':'2*log(phi)','ideal_triangle_thinness':'asinh(1)','matrix_M_squared_translation_length':'4*log(phi)'},
 'substitution_words':substitution,'golden_search':search,
 'cost':{'field_setup_and_initial_validation_ms':formation_ms,'all_construction_and_validation_ms':validation_ms,
         'peak_rss_raw':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
         'peak_rss_unit':'KiB' if sys.platform.startswith('linux') else 'platform-dependent',
         'research_network_and_report_time':'not included','word_formation_human_time':'not measured','search_candidates':0},
 'residuals':['No native adva/Rust implementation','No general knot invariant or faithful knot-group representation',
              'No complete Penrose or Borromean topology verifier','No certified transcendental evaluator',
              'No arbitrary-objective minimizer certificate','No universal grammar theorem']}
start=time.perf_counter();payload=json.dumps(result,ensure_ascii=False,indent=2)
decoded=json.loads(payload)
if decoded['check_count']!=len(checks):raise AssertionError('serialization replay')
result['cost']['serialization_and_parse_replay_ms']=(time.perf_counter()-start)*1000
print(json.dumps(result,ensure_ascii=False,indent=2))
