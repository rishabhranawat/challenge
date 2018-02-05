class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        max_len = 0
        max_word = ""
        for word in reversed(sorted(words, key=len)):
            found = True
            l = len(word)
            if(l < max_len):
                break
            for i in range(1, len(word), 1):
                if(word[:i] not in words):
                    found = False
                    break
            if(found):
                if(max_len < l):
                    max_len = l
                    max_word = word
                elif(max_len == l):
                    max_word = word if max_word > word else max_word
        return max_word
a = Solution()
print(a.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
        
                    
