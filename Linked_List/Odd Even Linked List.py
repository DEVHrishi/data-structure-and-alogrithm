'''Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]'''

'''approach:
1. two pointer
'''
# tc: O(n) and sc: O(n)
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead1 = ListNode(-1)
        oddHead = dummyHead1
        dummyHead2 = ListNode(-1)
        evenHead = dummyHead2

        currentNode = head
        count = 1
        while currentNode:
            if (count & 1) == 1:
                oddHead.next = currentNode
                oddHead = oddHead.next
            else:
                evenHead.next = currentNode
                evenHead = evenHead.next
            count += 1
            currentNode = currentNode.next
        oddHead.next = dummyHead2.next
        evenHead.next = None
        return dummyHead1.next
    
# tc: O(n) and sc: O(1)
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        oddHead = head
        evenHead = head.next
        even = evenHead
        while evenHead and evenHead.next:
            oddHead.next = evenHead.next
            oddHead = oddHead.next

            evenHead.next = oddHead.next
            evenHead = evenHead.next
        oddHead.next = even
        return head