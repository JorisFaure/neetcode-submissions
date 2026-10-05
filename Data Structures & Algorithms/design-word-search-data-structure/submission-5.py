class Word :
    def __init__(self) :
        self.children = {}
        self.isWord = False
class WordDictionary:

    def __init__(self):
        self.root = Word()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word :
            if c not in curr.children :
                curr.children[c] = Word()
            curr = curr.children[c]
        curr.isWord = True

        

    def search(self, word: str) -> bool:
        def dfs(root, word) :
            curr = root
            
            for i, c in enumerate(word) :
                if c == '.' :
                    for child in curr.children.values() :
                        if dfs(child, word[i+1::]) :
                            return True
                    return False
                if c not in curr.children :
                    return False
                curr = curr.children[c]
            return curr.isWord
        curr = self.root
        return dfs(curr, word)
