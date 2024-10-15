'''You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:


Build the result list and return its head.

Example 1:

Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [10,1,13,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
Example 2:


Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.'''

# tc: O(n) and sc: O(1)
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        currentNode = list1
        count = 1
        while currentNode:
            if count == a:  
                point1 = currentNode
            if count == b+1:
                point2 = currentNode
                
            count += 1
            currentNode = currentNode.next

        point1.next = list2
        point1 = point1.next
        while list2 and point1.next:
            point1 = point1.next
            list2 = list2.next
        point1.next = point2.next

        return list1