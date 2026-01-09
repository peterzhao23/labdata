import pandas as pd
#初始化行列名称表格
columns=[]
rows=[]
#获得需要提取的列名称
while True:
    
    while True:
        cs=int(input("请输入起始列"))
        ce=int(input("请输入终止列"))
        cskip=[]
        while True:
            c=input("请输入需要跳过的列")
            if c == "q":
                break
            else:
                cskip.append(int(c))


        clist=[]
        for i in range(cs,ce+1):
            if i not in cskip:
                clist.append(i-1)
            else:
                break


        columns=columns.extend(clist)
        break
        
            
#获得需要提取的行范围
    
    while True:
        rs=int(input("请输入起始行"))
        re=int(input("请输入终止行"))
        rows.extend([rs,re-rs+1])
        break
    break

df=pd.read_excel("LIQUID_VISCOSITY.xls",usecols=clist,skiprows=rows[0]-1,nrows=rows[1])
print(df)

  



        