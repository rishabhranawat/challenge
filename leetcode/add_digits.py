# Problem Source: LeetCode

# Given a non-negative integer num, repeatedly add all its digits 
# until the result has only one digit.

# For example:
# Given num = 38, the process is like: 3 + 8 = 11,
# 1 + 1 = 2. Since 2 has only one digit, return it.

# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?

### ### ###

# Garbage solution
def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    num_s = str(num)
    if(len(num_s) == 1): return num
    else:
        s = 0
        for nu in num_s:
            s += int(nu)
        return addDigits(s)

# The following is in constant time. It is using
# the digital root vedic formula [Used hint]
def addDigits(num):
    if(num == 0): return 0
    else: return (1 + (n-1)%9)