# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None): return None
        h = head
        curr = head.val
        new_head = ListNode(curr)
        ret = new_head
        while(h != None):
            if(h.val != curr):
                curr = h.val
                new_head.next = ListNode(curr)
                new_head = new_head.next
            h = h.next
        return ret
        
