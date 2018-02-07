class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace("-", "").upper()
        
        counter = K
        
        ans = []
        i = len(S)-K
        while(i >= 0):
            ans.extend(S[i:i+K][::-1])
            if(i > 0):
                ans.extend("-")
            i -= K
        if(i < 0):
            ans.extend(S[0:i+K][::-1])
        return str("".join(ans))[::-1]
            
a = Solution()
print(a.licenseKeyFormatting("5F3Z-2e-9-w",4))