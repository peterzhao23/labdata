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
uncertainty=Uncertainty()
dt=[1,2,3,4,5,6,7,8]
result=uncertainty.U(dt)
print(result)

