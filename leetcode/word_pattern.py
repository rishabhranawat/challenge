class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pairs = {}
        reversePairs ={}
        pattern_l = list(pattern)
        str_l = str.split(" ")
        if(len(pattern) != len(str_l)): return False
        if(pattern == str): return True
        for i in range(0, len(pattern_l), 1):
            p = pattern_l[i]
            s = str_l[i]
            if(p in pairs):
                if(pairs[p] != s): return False
            elif(s in reversePairs):
                if(reversePairs[s] != p): return False
            else:
                pairs[p] = s
                reversePairs[s] = p
        return True
        