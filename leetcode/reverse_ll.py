# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = []
        while(head != None):
            s.append(head.val)
            head = head.next

        ret = None
        ret_head = None
        for i in range(len(s)-1, -1, -1):
            each = s[i]
            if(ret == None):
                ret = ListNode(each)
                ret_head = ret
            else:
                ret.next = ListNode(each)
                ret = ret.next
        return ret_head