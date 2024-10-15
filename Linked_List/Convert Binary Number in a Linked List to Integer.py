'''Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

Example 1:

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0'''

'''approach:
1. using stack
2. bit manipulation'''

# tc: O(n) and sc: O(n)
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        stack = []
        currentNode = head
        while currentNode:
            stack.append(currentNode.val)
            currentNode = currentNode.next
        n = 0
        sum = 0
        while stack:
            sum += stack.pop() * (2**n)
            n += 1
        return sum

# tc: O(n) and sc: O(1)
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal_value = 0
        current = head
        while current:
            decimal_value = (decimal_value << 1) | current.val
            current = current.next
        return decimal_value
    
# tc: O(n) and sc: O(1)
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head: 
            ans = 2*ans + head.val 
            head = head.next 
        return ans 