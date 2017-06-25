class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret = list(secret)
        guessPairs = {}
        for i in range(0, len(guess), 1):
            num = guess[i]
            if(num in guessPairs):
                guessPairs[num].append(i)
            else:
                guessPairs[num] = [i]

        cowsBulls = {'A': 0, 'B':0}

        for i in range(0, len(secret), 1):
            num = secret[i]

            if(num in guessPairs):
                indx = guessPairs[num]
                for j in range(0, len(indx), 1):
                    ind = indx[j]
                    if(ind == i):
                        cowsBulls['A'] += 1
                        secret[i] = None
                        guessPairs[num][j] = -1
        
        for i in range(0, len(secret), 1):
            num = secret[i]
            if(num != None and num in guessPairs):
                indx = guessPairs[num]
                for j in range(0, len(indx), 1):
                    ind = indx[j]
                    if(ind != -1):
                        cowsBulls['B'] += 1
                        secret[i] = None
                        guessPairs[num][j] = -1
                        break

        ret = ""
        for key, value in cowsBulls.items():
            ret += str(value)+key 
        return ret

a = Solution()
print(a.getHint("11", "01"))
print(a.getHint("1123", "0111"))
print(a.getHint("1807", "7810"))