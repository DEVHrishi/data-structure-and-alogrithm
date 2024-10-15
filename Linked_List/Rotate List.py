'''Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]'''

#Optimal Approach T.C: O(N) S.C.: O(1)

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        curr = head
        size = 1

        # calculating length and making a circular loop
        while curr.next is not None:
            curr = curr.next
            size += 1

        curr.next = head

        # cut from the rotating point
        i = size - (k % size)

        while i > 1:
            head = head.next
            i -= 1

        curr = head.next
        head.next = None
        return curr