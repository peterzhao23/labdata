import sympy as sp
from data_extraction import roughcut,extract_numbers

n,p,p0,g,t,d,L,D=sp.symbols('n p p0 g t d L D') #变量符号化
U_p,U_p0,U_g,U_t,U_d,U_L,U_D=sp.symbols(' U_p U_p0 U_g U_t U_d U_L U_D') #不确定度符号化

Var= {
    
    'p':None,
    'p0':None,
    'g':None,
    't':None,
    'd':None,
    'L':None,
    'D':None,
    "U_p":None,
    "U_p0":None,
    "U_g":None,
    "U_t":None,
    "U_d":None,
    "U_L":None,
    "U_D":None
}#储存变量名与对应值的字典
var=[]

U=[U_p,U_p0,U_g,U_t,U_d,U_L,U_D]
n_ex=(1/18) * ((p - p0) * g * t * d**2) / (L * (1 + 2.4 * d / D)) #浮力计算公式
ln_n=sp.ln(n_ex) #对公式取对数
partials=[sp.diff(ln_n,var) for var in Var] #将不同变量的偏导存储在列表中

#合成总不确定度
E2=0   
for i in range(1,len(U)):
    E2=E2+(U[i]*partials[i])**2
E=E2**0.5 

#通过输入给变量赋值
for keys in Var.keys():
    i=input(f"请输入变量{keys}对应的值")
    Var[keys]=float(i)
#将表达式中元素替换为输入的值    
results=E.subs(Var)


class Uncertainty:
    def __init__(self):
        self.c=float(input("请输入置信系数"))
        self.ie=float(input("请输入仪器误差")) #instrument error
    def U(self,dt):
        n=len(dt)
        avr=sum(dt)/n
        Sa=(sum((i-avr)**2 for i in dt)/(n-1))**0.5
        Sa_=Sa/(n**0.5)
        Ub=abs(self.ie/self.c)
        U=(Sa_**2+Ub**2)**0.5
        result={
            "avr":avr,
            "Sa":Sa,
            "Sa_":Sa_,
            "Ua":Sa_,
            "Ub":Ub,
            "U":U
        }
        return result#返回平均值，标准偏差，算术平均值标准偏差的字典
    
read="LIQUID_VISCOSITY.xls"    
df=roughcut(read).fillna(0)#用零填充nan行
dfnum=df.map(extract_numbers)
cname=df.columns.to_list()

#按列处理数据
uncertainty=Uncertainty()
dfU=dfnum.apply(uncertainty.U)
    


            

  
