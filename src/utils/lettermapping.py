import pandas
def mapping(df,ex_dic): #输入表格的dataframe和包含公式所有信息的字典
    dfcol=df.columns.to_list()
    symbols=ex_dic["var"]
    character=[]
   # 并排显示版本 - 更紧凑
    print("变量列表与表格列对应：")
    print("-" * 40)

# 计算最大列数，使两栏对齐
    max_items = max(len(symbols), len(dfcol))

    print(f"{'变量 (数字)':<20} {'表格列 (字母)':<20}")
    print("-" * 40)
    col_mapping={}
    for i in range(max_items):
        var_str = f"{i+1:2d}. {symbols[i]}" if i < len(symbols) else ""
        col_str = ""
        if i < len(dfcol):
            letter = chr(65 + i).upper()
            character.append(letter) 
            col_str = f"{letter}. {dfcol[i]}"
            col_mapping[letter]=dfcol[i]
    
        print(f"{var_str:<20} {col_str:<20}")

    print("-" * 40)
    print("请将左侧变量(数字)与右侧列(字母)一一配对")
    map={}
    status=True
    while status:
        for i in symbols:
            while True:
                ask=input(f"请问{i}对应的列是？\n如果有，键入列编号；如果是常量，表格中没有，键入n\n").upper()
                if ask  in character:
                    map[i]=col_mapping[ask]
                    print("键入成功")
                    break
                elif ask=="N":
                    const=float(input("请键入常量的值"))
                    map[i]=const
                    print("键入成功")
                    break
                else:
                    print("请键入正确的字符！")
        print(map)
        while True:
            check=input("请检查，如果需要重新输入请键入r，不需要请键入n").upper()
            if check=="R":
                break
            elif check=="N":
                status=False
                break
            else:
                print("请键入正确的字母！")
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
    



        


   
