'''Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

Example 1:


Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
Example 2:


Input: root = [2,1,1]
Output: [[1]]
Example 3:


Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]'''

'''
1. encoded string
2. dfs'''

# tc = o(n^2) and sc = o(n)
class Solution:
  def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    ans = []
    count = collections.Counter()

    def encode(root: Optional[TreeNode]) -> str:
      if not root:
        return ''

      encoded = str(root.val) + '#' + \
          encode(root.left) + '#' + \
          encode(root.right)
      count[encoded] += 1
      if count[encoded] == 2:
        ans.append(root)
      return encoded

    encode(root)
    return ans

# tc = o(n) and sc = o(n)
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        
        seen = collections.defaultdict(int)
        res = []
        
        def helper(node):
            if not node:
                return
            sub = tuple([helper(node.left), node.val, helper(node.right)])
            print(sub)
            if sub in seen and seen[sub] == 1:
                res.append(node)
            seen[sub] += 1
            return sub
        
        helper(root)
        return res