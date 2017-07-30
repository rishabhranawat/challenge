# Problem Source: LeetCode
# Given a string, find the first non-repeating 
# character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

### ### ###
def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    data = {}
    if(len(s) == 0): return -1
    for i in range(0, len(s), 1):
        if(s[i] in data):
            data[s[i]][0] += 1
        else:
            data[s[i]] = [1, i]

    min_index = len(s)+1
    for key, val in data.items():
        if(val[0] == 1):
            index = val[1]
            if(index < min_index):
                min_index = index
    print(data)
    if(min_index < len(s)+1): 
        return min_index
    else: return -1

print(firstUniqChar("l"))