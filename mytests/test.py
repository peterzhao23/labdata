import sys
from pathlib import Path
currentdic=Path(__file__).parent.parent
sys.path.insert(0,str(currentdic))
from mytests import (
    roughcut,
    extract_numbers,
    coefi_writer,
    formal_dealer,
    Uncertainty,
    U,
    mapping,
    subdic
)
from src.config import TABLE_PATH
import pandas as pd
import sympy as sp
# 设置最大显示行数（None表示无限制）
pd.set_option('display.max_rows', None)

# 设置最大列宽（None表示无限制）
pd.set_option('display.max_colwidth', None)

# 设置显示完整内容不换行
pd.set_option('display.expand_frame_repr', False)

excelname=TABLE_PATH
df=roughcut(excelname)
dfnum=df.map(extract_numbers)
coef=coefi_writer()
coefi=dfnum.apply(coef)
U_=dfnum.apply(lambda series:U(series,coefi))
ex_latex=r"n_{\text{ex}} = \frac{(p - p_0) g t d^{2}}{18 L \left(1 + 2.4 \frac{d}{D}\right)}"
ex_dic=formal_dealer(ex_latex)
map=mapping(df,ex_dic)
map1=subdic(map,U_,ex_dic)
results=Uncertainty(map1)
print(results)

