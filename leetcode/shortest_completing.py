class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        letters =[]
        for each in licensePlate:
            if(not each.isdigit() and each != ' '):
                letters.append(each.lower())
        
        potent = []
        for word in words:
            h = {}
            for each in word:
                if(each in h):
                    h[each] += 1
                else:
                    h[each] =1 
            found = True
            print(letters, h)
            for l in letters:
                if l not in h:
                    found = False
                    break
                else:
                    h[l] -= 1

            for key, value in h.items():
                if(value < 0):
                    found = False

            if(found): potent.append((word, len(word)))

        potent.sort(key=lambda tup:tup[1])
        if(len(potent) > 0):
            return potent[0][0]
        return None

a = Solution()
print(a.shortestCompletingWord("1s3 PSt",["step", "steps", "stripe", "stepple"]))


