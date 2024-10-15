'''You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []'''

class Solution:
    def merge(self, l1, l2):
        dummyNode = ListNode(-1)
        dummy = dummyNode

        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2
        return dummyNode.next
    
    def partition(self, s, e, lists):
        if s == e:
            return lists[s]
        mid = s + (e-s)//2
        l1 = self.partition(s, mid, lists)
        l2 = self.partition(mid+1, e, lists)
        return self.merge(l1, l2)
        

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        s = 0
        e = len(lists) - 1
        return self.partition(s, e, lists)