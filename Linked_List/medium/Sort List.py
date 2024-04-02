'''Given the head of a linked list, return the list after sorting it in ascending order.
Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []'''

'''approach:
1. using stack
2. using merge sort
'''
# tc: O(nlogn) and sc: O(n)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        # define stack
        stack = []
        currentNode = head
        
        # store elements in stack
        while currentNode:
            stack.append(currentNode.val)
            currentNode = currentNode.next
            
        # sort the stack in descending order 
        stack.sort(reverse= True)
        
        # pop the elements and store it in new list
        dummyList = ListNode(-1)
        dummyHead = dummyList
        headNode = head
        while headNode:
            node=ListNode(stack.pop())
            dummyHead.next = node
            dummyHead=dummyHead.next
            headNode = headNode.next
            
        return dummyList.next
    
# tc: O(nlogn) and sc: O(1)
class Solution:
    def divide(self,head):
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    
    def Merge(self,l,r):
        temp=ans=ListNode()
        while l and r:
            if l.val<=r.val:
                temp.next=l
                l=l.next
            else:
                temp.next=r
                r=r.next
            temp=temp.next
        if l:
            temp.next=l
        if r:
            temp.next=r
        return ans.next
            
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left=head
        right=self.divide(head)
        temp=right.next
        right.next=None
        right=temp
        left=self.sortList(left)
        right=self.sortList(right)
        return self.Merge(left,right)