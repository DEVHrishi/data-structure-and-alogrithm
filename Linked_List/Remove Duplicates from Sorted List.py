'''Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummyNode = ListNode(-1)
        dummy = dummyNode

        curr = head
        while curr:
            dummy.next = curr
            temp = curr
            curr = curr.next
            while curr and temp.val == curr.val:
                dummy.next = curr
                curr = curr.next
            dummy = dummy.next
        return dummyNode.next