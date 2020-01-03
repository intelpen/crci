# Trie(also known as Prefix Tree_
# Is a n-tree where letters are stored in each node. We use "*" for leafs
# is mostly used for storing the dictionnary of a language for quick prefix lookups (O(K) time, J length of prefix)

# Implement a trie structure and check if a given string is a prefix of an existing word


class TrieNode:

    def __init__(self, letter, parent=None):
        self.letter = letter
        self.parent = parent
        self.childs_dict = {}


class Trie:

    def __init__(self):
        self.root = TrieNode("^")

    def check_prefix(self, prefix):
        current = self.root
        for character in prefix:
            if character in current.childs_dict:
                current = current.childs_dict[character]
            else:
                return False
        return True


trie = Trie()

a = TrieNode("a")
b = TrieNode("b")
c = TrieNode("c")
a.childs_dict = {"b": b, "c": c}
trie.root.childs_dict = {"a": a}

print(trie.check_prefix("ab"))
print(trie.check_prefix("abc"))
print(trie.check_prefix("c"))
print(trie.check_prefix("a"))
