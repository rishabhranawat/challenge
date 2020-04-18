# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        headS = head
        
        l = 0
        while(head):
            l += 1
            head = head.next
            
        mid = int(l/2)
        i = 0
        while(i < mid):
            headS = headS.next
            i += 1
        return headS