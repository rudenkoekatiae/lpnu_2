class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

def build_trie(patterns):
    trie = Trie()
    for word in patterns:
        trie.insert(word)
    return trie

patterns = ["cat", "cap", "can", "dog", "door"]
trie = build_trie(patterns)

print(trie.search("cat"))
print(trie.search("car"))       
print(trie.starts_with("ca"))
print(trie.starts_with("do"))
print(trie.starts_with("du"))
