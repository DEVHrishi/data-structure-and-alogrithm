'''Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []'''

class Solution:
    from collections import deque
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # check if root is none or not
        if not root:
            return []
        # define queue
        queue = deque([root])
        result = []
        direction = True
        # traverse the tree until queue is not empty
        while queue:
            level_size = len(queue)
            current_level = []
            for i in range(level_size):
                node = queue.popleft()
                if direction == True:
                    current_level.append(node.val)
                else:
                    current_level.insert(0, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            direction = not direction
            result.append(current_level)
        return result