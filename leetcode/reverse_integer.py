def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    if(x == 0): return 0
    ma = 2**31 - 1
    mi = - (ma)
    og = x
    if(x < 0):x = x*-1
    rev = ""
    while(x > 0):
        rev += str(x%10)
        x = x/10
    if(int(rev) < mi or int(rev) > ma): return 0
    else: 
        if(og < 0): return -int(rev)
        else: return int(rev)
            
        