# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if(head == None): return None
        ret = None
        ret_head = None
        h = head
        while(h != None):
            if(h.val != val):
                if(ret == None):
                    ret = ListNode(h.val)
                    ret_head = ret
                else:
                    ret.next = ListNode(h.val)
                    ret = ret.next
            h = h.next
        return ret_head