class Solution(object):
    def howMany(self, s, word):
        print()
        print()
        print(s, word)

        t = 0
        dict = list(word)
        target = list(s)
        
        for letter in dict:
            if(letter in target):
                index = target.index(letter)
                target[0:index+1]=[None]*(index+1)
                print(letter, target)
                t += 1
        return t
        
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        max_words = [""]
        max_len = -1
        for word in d:
            leng = self.howMany(s, word)
            if(leng >= max_len):
                max_len = leng
                max_words.append(word)
        counter = 0
        new_max = []
        print(max_len)
        while(counter < len(max_words)):
            each = max_words[counter]
            if(len(each) >= max_len):
                new_max.append(each)
            counter += 1
        return min(new_max)
a = Solution()
# print(a.findLongestWord("abpcplea", ["ale","apple","monkey","plea"]))
# print(a.findLongestWord("abpcplea", ["a","b","c"]))
# print(a.findLongestWord("apple", []))
print(a.findLongestWord("aewfafwafjlwajflwajflwafj",
["apple","ewaf","awefawfwaf","awef","awefe","ewafeffewafewf"]))