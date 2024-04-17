'''Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]'''

'''approach:
1. two pointer
'''

# tc: O(n) and sc: O(1)
class Solution:
    def reverseLinkedList(self, begin: Optional[ListNode], end: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while begin != end:
            next = begin.next
            begin.next = prev
            prev = begin
            begin = next

        return prev


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or head is None or head.next is None:
            return head
        
        dummy = ListNode(0, head)
        back, forward = dummy, head

        while back is not None:
            groupLen = 0
            while groupLen < k and forward is not None:
                forward = forward.next
                groupLen += 1
            
            if groupLen != k:
                break
            
            last = back.next

            back.next = self.reverseLinkedList(back.next, forward)
            
            last.next = forward
            back = last

        return dummy.next
