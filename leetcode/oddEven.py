# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddRetNode = None
        evenRetNode = None
        oddHead = None
        evenHead = None
        h = head
        counter = 1
        while(h != None):
            if(counter %2 ==0):
                if(evenRetNode == None):
                    evenRetNode = h
                    evenHead = evenRetNode
                else:
                    evenRetNode.next = h
                    evenRetNode = evenRetNode.next
            else:
                if(oddRetNode == None):
                    oddRetNode = h
                    oddHead = oddRetNode
                else:
                    oddRetNode.next = h
                    oddRetNode = oddRetNode.next
                    
            counter += 1
            h = h.next
        if(evenHead == None): return oddHead
        if(oddHead == None): return evenRetNode
        evenRetNode.next = None
        oddRetNode.next = evenHead
        return oddHead
            
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)

a3.next = a4
a2.next = a3
a1.next = a2

a = Solution()
k = a.oddEvenList(a1)

h = k
while(h != None):
    print(h.val)
    h = h.next

