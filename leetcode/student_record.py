# Problem Source: LeetCode

# You are given a string representing an attendance record for a student. 
# The record only contains the following three characters:

# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record 
# doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

# You need to return whether the student could be 
# rewarded according to his attendance record.

### ### ###

def checkRecord(s):
    """
    :type s: str
    :rtype: bool
    """
    ma = False
    count_a = 0
    mll = False
    i = 0
    while (i < len(s)):
        if(s[i] == 'A'):
            ma = ma + 1
            if(ma > 1): return False
        elif(s[i] == 'L' and (i+2 < len(s) 
            and (s[i+1] == 'L' and s[i+2] == 'L'))):
                 return False
        i += 1
    if(ma > 1): return False
    return True

print(checkRecord("PPALLP"))
print(checkRecord("PPALLL"))