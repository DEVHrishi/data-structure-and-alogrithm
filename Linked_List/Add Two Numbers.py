'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]'''

'''approach:
1. two pointer
'''
# tc: O(max(m,n)) and sc: O(max(m,n))
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummyList = ListNode(-1)
        dummyHead = dummyList

        while l1 or l2 or carry:
            sumValue = carry
            if l1:
                sumValue += l1.val 
                l1 = l1.next
            if l2:
                sumValue += l2.val
                l2 = l2.next

            carry = sumValue // 10
            node = sumValue % 10

            dummyHead.next = ListNode(node)
            dummyHead = dummyHead.next
        return dummyList.next