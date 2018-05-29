class Solution(object):
    def is_pal(self, word):
        return word == word[::-1]
    
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        index = {word: i for i, word in enumerate(words)}
        
        ret = []
        for j, word in enumerate(words):
            n = len(word)
            for i in xrange(0, n+1, 1):
                prefix = word[:i]
                suffix = word[i:]

                if(self.is_pal(prefix)):
                    b = suffix[::-1]
                    if(b != word and b in words):
                        ret.append((index[b], j))
                
                if(i != n and self.is_pal(suffix)):
                    b = prefix[::-1]
                    if(b != word and b in words):
                        ret.append((j, index[b]))
        return ret
        
a = Solution()
print(a.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
print(a.palindromePairs(["abcd","dcba","lls","s","sssll"]))