import pandas as pd
import re

#表格粗提取
def roughcut(excel):
    #初始化行列名称表格
    columns=[]
    rows=[]
    #获得需要提取的列名称
    while True:
    
        while True:
            cs=1 #int(input("请输入起始列"))
            ce=4 #int(input("请输入终止列"))
            cskip=[]
            while True:
                c="q"#input("请输入需要跳过的列,停止请键入q\n")
                if c == "q":
                    break
                else:
                    cskip.append(int(c))


            
            for i in range(cs,ce+1):
                if i not in cskip:
                    columns.append(i-1)
                else:
                    continue


            
            break
        
            
#获得需要提取的行范围
    
        while True:
            rs=3 #int(input("请输入起始行"))
            re=8 #int(input("请输入终止行"))
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


    


def U(series,coe): #计算不确定度   #用到df数据结构中，每一列变成一个series，coe是系数组成的series结构，索引是列名
        
    c=coe[series.name]["c"]
    ie=coe[series.name]["ie"]
    series=series.dropna()#删去nan
    n=len(series)

        
    avr=series.mean()
    Sa=(series.var()*n/(n-1))**0.5
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
    if pd.isna(result["Ua"]): #判断是否是nan
        result["U"]=Ub
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

#行数据间的计算 先最基本的四则运算
'''
def col_calculator(df):
    def col_collector():
        colname=[]
        while ask !="q":
            colname.append(int(ask)-1)
            ask=input("请问你需要对第几列进行操作？停止请键入q")
        return colname.sort()

    permission=input("你是否需要进行列之间的计算(y/n)")
    if permission=="n":
        return df
    else:
        tp=int(input("请问你需要进行哪一种运算，请键入数字" 
        "1.加法"
        "2.减法"
        "3.乘法"
        "4.除法"
        ))
        if tp==1 :
            colname1=col_calculator()
            mid1=df[colname1[0]]+df[colname1[]]
'''






        