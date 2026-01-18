
import sympy as sp
from latex2sympy2 import latex2sympy
def formal_dealer(latex_ex):
    sympy_expr=latex2sympy(latex_ex) #将latex公式转化为sympy公式
    symbols_in_expr=sorted(sympy_expr.free_symbols,key=str) #先提取所有自由变量为集合，在根据字符串排序转化为列表
    U=[sp.symbols(f"U{i}") for i in symbols_in_expr]
    #变量存储字典初始化
    sym_dic={}
    #i=0
    for symbols in symbols_in_expr:
        sym_dic[symbols]=None#i+1
        #i=i+1
    #j=0
    for u in U:
        sym_dic[u]=None#j+1
        #j=j+1
    ex_dic={}
    ex_dic["var"]=symbols_in_expr
    ex_dic["U"]=U
    ex_dic["values"]=sym_dic
    ex_dic["sympy_expression"]=sympy_expr
    ex_dic["latex_expression"]=latex_ex
    return ex_dic

def Uncertainty(ex_dic):#输入包含表达式所有信息的字典
    sympy_expr=ex_dic["sympy_expression"]
    symbols_in_expr=ex_dic["var"]
    U=ex_dic["U"]
    sym_dic=ex_dic["values"]
    ln_n=sp.ln(sympy_expr) #对公式取对数
    partials=[sp.diff(ln_n,var) for var in symbols_in_expr] 
#合成总不确定度
    E2=0
    for i in range(len(U)):
        E2=E2+(U[i]*partials[i])**2
    E=E2**0.5 
    var_dic={k:sym_dic[k] for k in symbols_in_expr}#只包含变量值的字典
    for values in var_dic.values():
        if values==None:
            a="输入值中包含None，请检查输入"
            return a
        else:
            continue
    expr_result=sympy_expr.subs(var_dic) #平均估计值
    results_E=E.subs(sym_dic)  #注意，替换的字典必须是由symbol对象和值构成的键值对组成的。
    results_U=results_E*abs(expr_result)
    results={}
    results["E"]=float(results_E)
    results["U"]=float(results_U)
    results["expr_values"]=float(expr_result)
    return results






            



