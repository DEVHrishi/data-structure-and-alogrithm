'''Given the root of a binary tree, return the sum of values of its deepest leaves.
 

Example 1:


Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19'''

# tc = o(n) and sc = o(h)
class Solution:
    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def dfs(self, root, height_of_tree, depth):
        if not root:
            return 0
        if depth == height_of_tree and not root.left and not root.right:
            return root.val
        return self.dfs(root.left, height_of_tree, depth+1) + self.dfs(root.right, height_of_tree, depth+1)

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # calculate height
        height_of_tree = self.height(root)
        return self.dfs(root, height_of_tree, 1)

# tc = o(n) and sc = o(w)
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        deepest_sum = 0

        while queue:
            level_size = len(queue)
            current_level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                current_level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            deepest_sum = current_level_sum
        
        return deepest_sum