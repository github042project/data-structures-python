class TrieNode:
    """
    Trie node class representing each character node in the Trie.
    Attributes:
        children (dict): Mapping from character to TrieNode.
        is_end_of_word (bool): True if node marks the end of a valid word.
    """
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """
    Trie (Prefix Tree) data structure for efficient prefix-based search.
    Supports insert, search, and prefix matching operations.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.
        Iteratively traverse the tree creating nodes for missing characters.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Search for a complete word in the Trie.
        Returns True if the word exists, False otherwise.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Check if there exists any word in the Trie that starts with the given prefix.
        Returns True if such prefix exists, False otherwise.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


if __name__ == "__main__":
    trie = Trie()
    words = ["hello", "hell", "heaven", "heavy"]
    for w in words:
        trie.insert(w)

    print(trie.search("hell"))     # True
    print(trie.search("hello"))    # True
    print(trie.search("he"))       # False
    print(trie.starts_with("hea")) # True
    print(trie.starts_with("hez")) # False
