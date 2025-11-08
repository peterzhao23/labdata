import sympy as sp

n,p,p0,g,t,d,L,D=sp.symbols('n p p0 g t d L D')
Var= {
    'n'=None,
    'p'=None,
    'p0'=None,
    'g'=None,
    't'=None,
    'd'=None,
    'L'=None,
    'D'=None
}

U_n,U_p,U_p0,U_g,U_t,U_d,U_L,U_D=sp.symbols('U_n U_p U_p0 U_g U_t U_d U_L U_D')
U=[U_n,U_p,U_p0,U_g,U_t,U_d,U_L,U_D]
n_ex=(1/18) * ((p - p0) * g * t * d**2) / (L * (1 + 2.4 * d / D))
ln_n=sp.ln(n_ex)
partials=[sp.diff(ln_n,var) for var in Var]
E2=(U[1]*partials[1])**2
for i in range(2,len(U)):
    E2=E2+(U[i]*partials[i])**2

E=E2**0.5 


for i in Var:
    var=Var[i]
    =input("请输入变量{Var[i]}对应的值")

  
