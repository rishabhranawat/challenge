# Problem Source: LeetCode
# Given a word, you need to judge whether 
# the usage of capitals in it is right or not.

# We define the usage of capitals in a word to be 
# right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital if 
# it has more than one letter, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.

### ### ###
def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    word_upper = word.upper()
    if(word == word_upper): return True
    else:
        if(word[0].upper() == word_upper[0] and word[1:] == word[1:].lower()): 
            return True
        else:
            if(word.lower() == word): return True
            else: return False
print(detectCapitalUse("usA"))