from pathlib import Path
import sys
testpath=Path(__file__).parent.parent
sys.path.insert(0,str(testpath))     
from src.utils import (
    roughcut,
    extract_numbers,
    coefi_writer,
    formal_dealer,
    Uncertainty,
    U,
    mapping
)
from src.config import TABLE_PATH
import pandas as pd

# 设置最大显示行数（None表示无限制）
pd.set_option('display.max_rows', None)

# 设置最大列宽（None表示无限制）
pd.set_option('display.max_colwidth', None)

# 设置显示完整内容不换行
pd.set_option('display.expand_frame_repr', False)

excelname=TABLE_PATH
df=roughcut(excelname)
ex_latex=r"n_{\text{ex}} = \frac{(p - p_0) g t d^{2}}{18 L \left(1 + 2.4 \frac{d}{D}\right)}"
ex_dic=formal_dealer(ex_latex)
mapping(df,ex_dic)


