# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        all_A = set()
        hA = headA
        while(hA != None):
            all_A.add(hA)
            hA = hA.next
        hB = headB
        while(hB != None):
            if(hB in all_A): return hB
            else: all_A.add(hB)
            hB = hB.next
        return None