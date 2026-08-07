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
        curr_node = self.begin
        o_len = len(word)
        def rec(curr_node, word, o_len) :
            for i, c in enumerate(word) :
                if c in curr_node.children :
                    curr_node = curr_node.children[c]
                elif c == '.' :
                    if i == o_len - 1 :
                        return curr_node.endOfWord
                    for k in curr_node.children.keys() :
                        if rec(curr_node.children[k], word[i+1:], o_len) :
                            return True
                    return False
                else :
                    return False
            return curr_node.endOfWord
        return rec(curr_node, word, o_len)
        
