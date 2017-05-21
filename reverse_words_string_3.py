# Problem Source: LeetCode

# Given a string, you need to reverse the order of characters in 
# each word within a sentence while still 
# preserving whitespace and initial word order.

# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space 
# and there will not be any extra space in the string.

### ### ###

# O(n^2)
def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    ret_str = ""
    words = s.split(" ")
    for word in words:
        rev_word = ""
        for i in range(len(word)-1, -1, -1):
            rev_word += word[i]
        ret_str += " "+rev_word
    return ret_str.strip()

# O(n)
def reverseWords2(s):
    ret_str = ""
    word = ""
    for letter in s:
        if(letter == " "):
            ret_str += " "+word
            word = ""
        else:
            word = letter + word
    return (ret_str+" "+word).strip()

print(reverseWords2("Let's take LeetCode contest").strip())

            