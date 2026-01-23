import pandas
def mapping(df,ex_dic): #输入表格的dataframe和包含公式所有信息的字典
    dfcol=df.columns.to_list()
    symbols=ex_dic["var"]
    map={}
    map[symbols[0]]=0.1
    map[symbols[1]]=dfcol[3]
    map[symbols[2]]=dfcol[0]
    map[symbols[3]]=9.8
    map[symbols[4]]=10.0
    map[symbols[5]]=1.0
    map[symbols[6]]=dfcol[1]

    
    return map

def subdic(map,U_,exdic):    #键入map字典，U_字典，和exdic字典。即输入替换标准以及表达式和不确定度的所有信息
    keys=list(exdic["values"].keys())
    lenth=int(len(keys)/2)
    i=0
    for name,values in map.items():
        if type(values)== float:
            exdic["values"][keys[lenth+i]]=0       #不是表格给定的量默认常量，不确定度为0
            exdic["values"][name]=map[name]
        else:
            exdic["values"][name]=float(U_[values]["avr"])
            exdic["values"][keys[lenth+i]]=float(U_[values]["U"])
        i+=1
    return exdic


        


   
