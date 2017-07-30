def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    nums = {'IV':4, 'XL':40, 'XC':90, 'CD':400,
    'CM':900,'D': 500, 'M':1000, 'C':100, 'L':50, 'X': 10, 'IX':9, 'V':5, 'I': 1}
    i = 0
    total = 0
    while(i < len(s)):
        if(i+1 < len(s) and s[i]+s[i+1] in nums):
            total += nums[s[i]+s[i+1]]
            i += 2
        else:
            total += nums[s[i]]
            i+=1
    return total

print(romanToInt('IX'))
print(romanToInt('IIII'))
print(romanToInt('V'))
print(romanToInt('VI'))
print(romanToInt('XI'))
print(romanToInt('MCMXCVI'))