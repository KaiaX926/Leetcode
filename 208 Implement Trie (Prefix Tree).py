class Trie:

    def __init__(self):
        self.trie = []
        

    def insert(self, word: str) -> None:
        self.trie.append(word)
        return 

        
    def search(self, word: str) -> bool:
        return word in self.trie
        

    def startsWith(self, prefix: str) -> bool:
        for i in self.trie:
            if i[:len(prefix)] == prefix:
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
