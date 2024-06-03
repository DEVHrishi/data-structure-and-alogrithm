'''Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.

 

Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []'''

class Solution:
    def createList(seld, head, list):
        if not head:
            return
        while head:
            list.append(head.val)
            head = head.next

    def binaryTree(self, l, r, arr):
        if l > r:
            return
        length = len(arr)
        mid = (l+r) // 2
        root = TreeNode(arr[mid])
        root.left = self.binaryTree(l, mid-1, arr)
        root.right = self.binaryTree(mid+1, r, arr)
        return root
        
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return 
        linked_list = []
        self.createList(head, linked_list)
        print(linked_list)
        return self.binaryTree(0, len(linked_list)-1, linked_list)
    
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head==None:
            return None
        if head.next==None:
            return TreeNode(head.val)
        slow,fast=head,head.next
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next
        slow.next=None
        root=TreeNode(mid.val)
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(mid.next)
        return root