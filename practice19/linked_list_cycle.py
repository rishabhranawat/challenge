# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodes = set()
        
        while(head):
            
            start = head.next
            while(start):
                if(start == head):
                    return True
                start = start.next
            head = head.next

        return False

l1 = ListNode(3)
l2 = ListNode(2)
l3 = ListNode(0)
l4 = ListNode(-4)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l2

a = Solution()
a.hasCycle(l1)
            