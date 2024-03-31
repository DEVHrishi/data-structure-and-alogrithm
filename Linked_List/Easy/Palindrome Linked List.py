'''Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false'''

'''approach:
1. using set
2. 2 pointer fast and slow where reverse the second half of the list then check
'''
# tc: O(n) and sc: O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        currentNode = head
        while currentNode:
            stack.append(currentNode.val)
            currentNode = currentNode.next
        headNode = head
        
        while headNode:
            if headNode.val != stack.pop():
                return False
            headNode = headNode.next
        return True
    
# tc: O(n) and sc: O(1)
class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        previous_node = None
        current_node = head
        while current_node:
            nextNode = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = nextNode
        return previous_node


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        pointer = self.reverse(slow)
        while pointer:
            if pointer.val != head.val:
                return False
            pointer = pointer.next
            head = head.next
        return True