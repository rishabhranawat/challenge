# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        head = head
        
        while(head.next != None):
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        head.next = prev
        return head

a = Solution()
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)
a6 = ListNode(6)


a5.next = a6
a4.next = a5
a3.next = a4
a2.next = a3
a1.next = a2
h = a.reverseList(a1)

while(h != None):
    print(h.val)
    h = h.next
