class TrieNode(object):
    def __init__(self):
        self.next ={}
        self.eof = False

class Trie(object):
    

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        head = self.root
        for i in range(0, len(word), 1):
            letter = word[i]
            if(letter in head.next):
                head = head.next[letter]
                if(i == len(word)-1):
                    head.eof = True
            else:
                head.next[letter] = TrieNode()
                head = head.next[letter]
                if(i == len(word)-1):
                    head.eof = True
                    
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        head = self.root
        counter = 0
        w = ""
        while(head != None and counter < len(word)):
            letter = word[counter]
            if(letter not in head.next): 
                return False
            else:
                head = head.next[letter]
            counter += 1
            w += letter
            
        if(head.eof == True and w == word): return True
        else: return False 

        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        head = self.root
        counter = 0
        w = ""
        while(head != None and counter < len(prefix)):
            letter = prefix[counter]
            if(letter not in head.next): return False
            else:
                head = head.next[letter]
                w += letter
            counter += 1
        if(w == prefix): return True
        else: return False
        
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
word = "abc"
obj.insert("abc")

print(obj.startsWith(word))
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)