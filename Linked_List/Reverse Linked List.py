'''Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []'''

'''approach: 
1. using stack, 
2. use 3 pointer approach change in place direction of link, 
3. recursive '''

# tc: O(n) and sc: O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        list_head = head
        while list_head:
            stack.append(list_head.val)
            list_head = list_head.next

        reverse_list_head = head
        while reverse_list_head:
            reverse_list_head.val = stack.pop()
            reverse_list_head = reverse_list_head.next
        return head

# tc: O(n) and sc: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = None
        current_node = head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        return previous_node
    
# tc: O(n) and sc: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        next_node = head.next
        next_node.next = head
        head.next = None
        return new_head