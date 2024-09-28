'''Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def traverse(self, result, path):
        node = self.root
        def dfs(node, path, result):
            if path:
                result.append(int(path))
            for i in node.children.keys():
                dfs(node.children[i], path+i, result)
        dfs(node, path, result)
        

    def lexicalOrder(self, n: int) -> List[int]:
        # create TrieNode
        # insert operation
        for i in range(1, n+1):
            self.insert(str(i))

        print(self.root.children.keys())
        # search operation
        result = []
        self.traverse(result, '')
        return result
    
    
def lexicalOrder(self, n: int) -> List[int]:
	ans = []
	def dfs(s):
		ans.append(int(s))
		for i in range(10):
			if(int(s+str(i)) > n):
				return
			else:
				if(s): dfs(s+str(i))

	for i in range(1, min(n+1, 10)): dfs(str(i))
	return ans