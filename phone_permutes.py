class Solution(object):
    permutations = []
    def permuteBacktrack(self, counter, level, result, s):
        if(level == len(s)):
            r = ""
            for each in result:
                r += each
            self.permutations.append(r)
            return
        for i in range(0, len(s), 1):
            if(counter[i] == 0):
                continue
            result[level] = s[i]
            counter[i] -= 1
            self.permuteBacktrack(counter, level+1, result, s)
            counter[i] += 1

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        
        return self.permutations
