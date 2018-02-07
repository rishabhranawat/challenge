class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        og = 2*len(B)
        add = A
        counter = 1
        while(len(A) <= og):
            if(B in A): return counter
            A = A+add
            counter+= 1
        if(B in A): return counter

        return -1
a = Solution()
print(a.repeatedStringMatch("bcacbcbbbbbbbacbcaacbccaa",
"bbcacbcbbbbbbbacbcaacbccaacbcacbcbbbbbbbacbcaacbccaaabcacbcbbbbbbbacbcaacbccaacbcacbcbbbbbbbacbcaacbccaabbcacbcbbbbbbbacbcaacbccaacbcacbcbbbbbbbacbcaacbccaabbcacbcbbbbbbbacbcaacbccaabbcacbcbbbbbbbacbcaacbccaabbcacbcbbbbbbbacbcaacbccaabbcacbcbbbbbbbacbcaacbccaabbcacbcbbbbbbbacbcaacbccaabbcacbcbbbbbbbacbcaacbccaabbcacbcbbbbbbbacbcaacbccaaabcacbcbbbbbbbacbcaacbccaacbcacbcbbbbbbbacbcaacbccaabbcacbcbbbbbbbacbcaacbccaacbcacbcbbbbbbbacbcaacbccaaabcacbcbbbbbbbacbcaacbccaaabcacbcbbbbbbbacbcaacbccaacbcacbcbbbbbbbacbcaacbccaabbcacbcbbbbbbbacbcaacbccaacbcacbcbbbbbbbacbcaacbccaacbcacbcbbbbbbbacbcaacbccaaabcacbcbbbbbbbacbcaacbccaaa"))