'''You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]'''

'''approach:
1. reverse the lists then add values and again reverse
'''

# tc: O(max(m,n)) and sc: O(1)
class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reverse_l1 = self.reverseList(l1)
        reverse_l2 = self.reverseList(l2)

        dummyList = ListNode(-1)
        dummyHead = dummyList
        carry = 0

        while reverse_l1 or reverse_l2 or carry:
            sum_value = carry
            if reverse_l1:
                sum_value += reverse_l1.val
                reverse_l1 = reverse_l1.next

            if reverse_l2:
                sum_value += reverse_l2.val
                reverse_l2 = reverse_l2.next
            
            carry = sum_value // 10
            node = sum_value % 10

            dummyHead.next = ListNode(node)
            dummyHead = dummyHead.next
        
        reverse_dummy = self.reverseList(dummyList.next)
        return reverse_dummy
        

    def reverseList(self, l: Optional[ListNode]) -> Optional[ListNode]:
        previousNode = None 
        currentNode = l
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
        return previousNode
    
# tc: O(m+n) and sc: O(m+n)
class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []

        while l1 or l2:
            if l1:
                stack1.append(l1.val)
                l1 = l1.next
            if l2:
                stack2.append(l2.val)
                l2 = l2.next
        
        result = None
        carry = 0

        while stack1 or stack2 or carry:
            sum_value = carry
            if stack1:
                value1 = stack1.pop()
                sum_value += value1
            if stack2:
                value2 = stack2.pop()
                sum_value += value2
            

            carry = sum_value // 10
            node = sum_value % 10

            dummyNode = ListNode(node)
            dummyNode.next  = result
            result = dummyNode
        
        return result
