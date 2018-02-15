# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, K):
    # write your code in Python 3.6
    s = S.upper().replace("-", "")
    res = ""
    i = len(s)-1
    
    while(i > 0):
    	ne = s[i-K+1:i+1][::-1]
        res += ne+"-"
        i -= K

    if(i == 0):
    	res += s[0]
    elif(i < 0):
    	res += s[0:abs(i)]
    print(res[::-1])
    return res
a = solution('2-4A0r7-4k', 3) 