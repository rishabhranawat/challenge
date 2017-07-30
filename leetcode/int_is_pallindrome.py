def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if(x < 0): x = -1*x
    if(x == 0): 
    	return True
    og = x
    num = ""
    place = 1
    while(x > 0):
    	dig = x % 10
    	num =  num+str(dig)
    	x = x/10
    print(int(num) == og)

isPalindrome(0)

            