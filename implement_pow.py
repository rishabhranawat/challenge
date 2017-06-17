def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if(n == 1): return x
    elif(n == -1): return 1/x
    if(n == 0): return 1
    elif(n > 0):
        return x*self.myPow(x, n-1)
    else:
        return x*self.myPow(x, n+1)

def myPow2(x, n):
    if(n == 0): return 1
    if(n <0):
        x = 1/x
        n = n * -1
    val = 1
    while(n >= 1):
        val = val*x
        n -= 1
    return val


print(myPow2(1.00001, 123456))