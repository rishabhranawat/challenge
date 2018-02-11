class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.abbrs = {}
        for each in dictionary:
            ab = self.getAbbreviation(each)
            
            if(ab in self.abbrs):
                self.abbrs[ab].add(each)
            else:
                self.abbrs[ab] = set()
                self.abbrs[ab].add(each)
        
    
    def getAbbreviation(self, word):
        if(len(word) == 0): return None
        return word[0]+str(len(word[:-1]))+word[-1]

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        ab = self.getAbbreviation(word)
        if(ab not in self.abbrs):
            return True
        elif(len(self.abbrs[ab]) > 1):
                return False
        elif(len(self.abbrs[ab]) == 1 and word not in self.abbrs[ab]):
            return False

        return True


# Your ValidWordAbbr object will be instantiated and called as such:
obj = ValidWordAbbr(["a", "a"])
print(obj.isUnique("a"))