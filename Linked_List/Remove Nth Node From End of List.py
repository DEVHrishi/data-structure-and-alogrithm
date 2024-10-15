'''Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]'''

'''approach:
1. use single pointer
2. fast and slow approach
'''
# tc: O(n) and sc: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # list is empty or not
        if head.next is None:
            return None

        #create dummy node and point to head
        dummyNode = ListNode(-1)
        dummyNode.next = head
        currentNode = dummyNode

        # calculate length of the list
        length = 0
        tempNode = dummyNode
        while tempNode:
            length += 1
            tempNode = tempNode.next
        
        # traverse the list and find the index and remove it
        count = 1
        position = length - n
        while currentNode:
            if count == position:
                currentNode.next = currentNode.next.next
                break
            count += 1
            currentNode = currentNode.next
        return dummyNode.next

# tc: O(n) and sc: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast=head
        slow=head
        for _ in range(n):
            fast=fast.next
        if not fast: return head.next
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head