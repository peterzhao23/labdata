import pandas as pd
import re


def roughcut(excel):
    #初始化行列名称表格
    columns=[]
    rows=[]
    #获得需要提取的列名称
    while True:
    
        while True:
            cs=1 #int(input("请输入起始列"))
            ce=9 #int(input("请输入终止列"))
            cskip=[]
            while True:
                c="q"#input("请输入需要跳过的列")
                if c == "q":
                    break
                else:
                    cskip.append(int(c))


            
            for i in range(cs,ce+1):
                if i not in cskip:
                    columns.append(i-1)
                else:
                    break


            
            break
        
            
#获得需要提取的行范围
    
        while True:
            rs=3#int(input("请输入起始行"))
            re=28#int(input("请输入终止行"))
            rows.extend([rs,re-rs+1])
            break
        break
    df=pd.read_excel(excel,usecols=columns,skiprows=rows[0]-1,nrows=rows[1])
    return df





#  使用正则表达式提取所有数字（包括小数）
def extract_numbers(text):
    # 查找所有数字（包括小数）
    numbers = re.findall(r'\d+\.?\d*', str(text))
    # 转换为浮点数或整数
    if numbers:
        try:
            # 如果是整数，转换为int，否则float
            num = float(numbers[0])
            return int(num) if num.is_integer() else num
        except:
            return None
    return None


    
read="LIQUID_VISCOSITY.xls"    
df=roughcut(read)
dfnum=df.map(extract_numbers)
cname=df.columns.to_list()

def U(series,coe): #计算不确定度   #用到df数据结构中，每一列变成一个series，coe是系数组成的series结构，索引是列名
        
    c=coe[series.name]["c"]
    ie=coe[series.name]["ie"]
    series=series.dropna()#删去nan
    n=len(series)

        
    avr=series.mean()
    Sa=(series.var()/(n-1))**0.5
    Sa_=Sa/(n**0.5)
    Ub=abs(ie/c)
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

#使用工厂函数，对每一列的数据都生成对应的处理函数
def coefi_writer():
    params={}#以下函数运行结果的缓存

    
    def check_writer(series):#apply时每组构成新的数据类型series
        col=series.name #提取名称
        cc=f"{col}的置信系数"
        iec=f"{col}的仪器误差"
        if col in params:
            a=input(("是否需要重新输入？y/n"))
            if a == "y":
                params[col]={"c":float(input(f"请输入{cc}")),"ie":float(input(f"请输入{iec}"))}
                
        else:
            params[col]={"c":float(input(f"请输入{cc}")),"ie":float(input(f"请输入{iec}"))}
        return params[col] #调用U函数计算
    return check_writer

    
coef=coefi_writer()
coefi=df.apply(coef)  #让用户键入所有系数
U_=df.apply(lambda series:U(series,coefi))
print(U_)





        