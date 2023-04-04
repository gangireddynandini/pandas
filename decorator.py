def getval():
    return float(input('enter any numerical value:'))
def calsquare(getval):
    def oper():
        n=getval()
        res=n**2
        return res
    return oper
dij=calsquare(getval)
e=dij()
print('square',e)