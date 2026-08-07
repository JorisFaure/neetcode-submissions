class TrieNode :
    def __init__(self) :
        self.children = {}
        self.isEndOfWord = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        i = 0
        head = self.root
        while i < len(word) and word[i] in self.root.children :
            self.root = self.root.children[word[i]]
            i+=1
        while i < len(word) :
            self.root.children[word[i]] = TrieNode()
            self.root = self.root.children[word[i]]
            i+=1
        self.root.isEndOfWord = True
        self.root = head




    def search(self, word: str) -> bool:
        i = 0
        head = self.root
        while i < len(word) and word[i] in head.children :
            head = head.children[word[i]]
            i+=1
        if i == len(word) and head.isEndOfWord == True :
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        i = 0
        head = self.root
        while i < len(prefix) and prefix[i] in head.children :
            head = head.children[prefix[i]]
            i+=1
        if i == len(prefix) :
            return True
        return False
        