class Letter :
    def __init__(self) :
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Letter()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word :
            if c not in curr.children :
                curr.children[c] = Letter()
            curr = curr.children[c]
        curr.isEndOfWord = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        def search_(word, curr) :
            for i, c in enumerate(word) :
                print(i, word, c, curr.children)
                if c in curr.children :
                    curr = curr.children[c]
                    continue
                if c != '.' :
                    return False
                if c == '.' :
                    for child in curr.children :
                        if search_(word[i+1:], curr.children[child]) :
                            return True
                    return False
            if curr.isEndOfWord == False :
                return False
            return True
        return search_(word, curr)
