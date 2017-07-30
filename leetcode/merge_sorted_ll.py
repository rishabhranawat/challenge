# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head1 = l1
        head2 = l2

        ret = None
        retHead = None

        while(head1 != None or head2 != None):
            if(head1 and head2):
                new = None
                if(head1.val < head2.val):
                    new = ListNode(head1.val)
                    head1 = head1.next
                else:
                    new = ListNode(head2.val)
                    head2 = head2.next

                if(ret == None):
                    retHead = new
                    ret = new
                else:
                    ret.next = new
                    ret = ret.next
            else:
                if(head1 == None):
                    if(ret == None): return head2
                    else:
                        ret.next = head2
                        return retHead
                else:
                    if(ret == None): return head1
                    else:
                        ret.next = head1
                        return retHead
                
        return retHead
            
                    
