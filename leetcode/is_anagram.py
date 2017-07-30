# Problem Source: LeetCode

# Given two strings s and t, write a 
# function to determine if t is an anagram of s.

# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.

### ### ###

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    letters = {}
    if(len(s) != len(t)): return False
    for each in s:
        if(each in letters): 
            letters[each] += 1
        else:
            letters[each] = 1
    
    for letter in t:
        if(letter in letters):
            if(letters[letter] > 0):
                letters[letter] -= 1
            else:
                return False
        else:
            return False
    return True

print(isAnagram("ab", "a"))