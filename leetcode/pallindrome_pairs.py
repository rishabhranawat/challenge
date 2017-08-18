class Solution(object):
    def isPallindrome(self, word):
        start = 0
        end = len(word)-1
        while(start < end):
            if(word[end] != word[start]): return False
            start += 1
            end -= 1
        return True
    
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ret = []
        for i in range(0, len(words), 1):
            for j in range(0, len(words),1):
                if(i == j): continue
                else:
                    if(self.isPallindrome(words[i]+words[j])):
                        ret.append([i, j])
        return ret
a = Solution()
print(a.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))