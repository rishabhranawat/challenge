def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    neg = False
    if(x < 0):
        neg = True
        x = -1*x
        
    x = list(str(x))
    start = 0
    end = len(x)-1
    while(start <= end):
        temp = x[start]
        x[start] = x[end]
        x[end] = temp
        start += 1
        end -= 1
    x = "".join(x)
    if(neg): return int("-"+x)
    else: return int(x)

def reverse(x):
    int ret = 0
    while(x != 0):
        ret = ret*10 + x % 10
        x = x/10
    return ret
