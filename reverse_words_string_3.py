# Horrible Runtime.
# Will getback to it in a bit.

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

print(reverseWords("Let's take LeetCode contest").strip())

            