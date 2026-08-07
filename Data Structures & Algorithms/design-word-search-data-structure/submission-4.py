class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.begin = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr_node = self.begin
        for c in word :
            if not c in curr_node.children :
                curr_node.children[c] = TrieNode()
            curr_node = curr_node.children[c]
        curr_node.endOfWord = True

    
        

    def search(self, word: str) -> bool:
        def rec(i, curr_node) :
            for j in range(i, len(word)) :
                if word[j] in curr_node.children :
                    curr_node = curr_node.children[word[j]]
                elif word[j] == '.' :
                    for child in curr_node.children.values() :
                        if rec(j+1, child) :
                            return True
                    return False
                else :
                    return False
            return curr_node.endOfWord
        curr_node = self.begin
        return rec(0, curr_node)
        
