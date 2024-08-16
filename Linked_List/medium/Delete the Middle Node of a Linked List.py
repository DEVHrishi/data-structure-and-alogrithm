'''You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 
Example 1:
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
Example 2:


Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
Example 3:


Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.'''

'''approach:
1. single pointer approach
2. two pointer or fast and slow approach
'''
# tc: O(n) and sc: O(1)
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        # calculate the length of the list
        length = 0
        headNode = head
        while headNode:
            length += 1
            headNode = headNode.next

        # traverse upto the middle of the list and remove the middle of the list
        
        currentNode = head
        length = length // 2
        while currentNode:
            length -= 1
            if length == 0:
                currentNode.next = currentNode.next.next
                break
            
            currentNode = currentNode.next
        return head
    
# tc: O(n) and sc: O(1)
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        # using two pointer traverse upto the middle element and get the previous value of middle element
        slow = head
        fast = head
        previousNode = None

        while fast and fast.next:
            previousNode = slow
            slow = slow.next
            fast = fast.next.next
        previousNode.next = previousNode.next.next
        return head