'''Ninja has to implement a data structure ”TRIE” from scratch. Ninja has to complete some functions.

1) Trie(): Ninja has to initialize the object of this “TRIE” data structure.

2) insert(“WORD”): Ninja has to insert the string “WORD”  into this “TRIE” data structure.

3) countWordsEqualTo(“WORD”): Ninja has to return how many times this “WORD” is present in this “TRIE”.

4) countWordsStartingWith(“PREFIX”): Ninjas have to return how many words are there in this “TRIE” that have the string “PREFIX” as a prefix.

5) erase(“WORD”): Ninja has to delete one occurrence of the string “WORD” from the “TRIE”.
Note:

1. If erase(“WORD”) function is called then it is guaranteed that the “WORD” is present in the “TRIE”.

2. If you are going to use variables with dynamic memory allocation then you need to release the memory associated with them at the end of your solution.
Can you help Ninja implement the "TRIE" data structure?'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_count = 0  # Count of words ending at this node
        self.prefix_count = 0  # Count of words passing through this node

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1
        node.end_count += 1

    def countWordsEqualTo(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.end_count

    def countWordsStartingWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.prefix_count

    def erase(self, word):
        def erase_helper(node, word, index):
            if index == len(word):
                if node.end_count > 0:
                    node.end_count -= 1
                    node.prefix_count -= 1
                    return node.prefix_count == 0
                return False

            char = word[index]
            if char not in node.children:
                return False

            child = node.children[char]
            should_delete_child = erase_helper(child, word, index + 1)

            if should_delete_child:
                del node.children[char]

            node.prefix_count -= 1
            return node.prefix_count == 0 and not node.end_count

        erase_helper(self.root, word, 0)
