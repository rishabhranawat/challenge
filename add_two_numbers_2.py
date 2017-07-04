# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getNumber(self, n):
        h = n
        s = ""
        while(h != None):
            s += str(h.val)
            h = h.next
        return int(s)
            
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = self.getNumber(l1)
        n2 = self.getNumber(l2)
        k = list(str(n1+n2))
        ret = None
        retHead = None
        for each in k:
            n = ListNode(each)
            if(ret == None):
                ret = n
                retHead = ret
            else:
                ret.next = n
                ret = ret.next
        return retHead
        