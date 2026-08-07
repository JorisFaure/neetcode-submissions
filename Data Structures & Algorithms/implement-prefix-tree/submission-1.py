class TrieNode :
    def __init__(self) :
        self.isEndOfWord = False
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.begin = TrieNode()
        

    def insert(self, word: str) -> None:
        curr_node = self.begin
        for i, c in enumerate(word) :
            if not c in curr_node.children :
                curr_node.children[c] = TrieNode()
            curr_node = curr_node.children[c]
        curr_node.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr_node = self.begin
        for c in word :
            if not c in curr_node.children :
                return False
            curr_node = curr_node.children[c]
        return curr_node.isEndOfWord


    def startsWith(self, prefix: str) -> bool:
        curr_node = self.begin
        for i in range(len(prefix)) :
            if prefix[i] not in curr_node.children :
                return False
            curr_node = curr_node.children[prefix[i]]
        return True
        