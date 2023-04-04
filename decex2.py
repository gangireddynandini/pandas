def calsqr(getval):
    def operation():
        n=getval()
        res=n**3
        return res
    return operation
def calsqu(getval):
    def operation():
        n=getval()
        res=n**4
        return res
    return operation
@calsqr
def getval():
    return float(input('enter num val:'))
@calsqu
def getval2():
    return float(input('enter any numeri val:'))
t=getval()
print(t)
y=getval2()
print(y)
