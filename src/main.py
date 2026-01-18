import sys
from pathlib import Path
from utils import (
    roughcut,
    extract_numbers,
    coefi_writer,
    formal_dealer,
    Uncertainty,
    U
)
from config import TABLE_PATH
def main():
    excelname=TABLE_PATH
    df=roughcut(excelname)
    dfnum=df.map(extract_numbers)
    coef=coefi_writer()
    coefi=dfnum.apply(coef)
    U_=dfnum.apply(lambda series:U(series,coefi))
    ex_latex=r"n_{\text{ex}} = \frac{(p - p_0) g t d^{2}}{18 L \left(1 + 2.4 \frac{d}{D}\right)}"
    ex_dic=formal_dealer(ex_latex)
    sym_dic=ex_dic["values"]
    



