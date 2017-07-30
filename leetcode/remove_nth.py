# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = 0
        lenNode = head
        while(lenNode != None):
            l += 1
            lenNode = lenNode.next

        if(head == None): return None

        h = head
        prev = None
        ind = l-n
        
        while(ind > 0):
            prev = h
            h = h.next
            ind -= 1
        
        if(h != None):
            temp = h.next
            if(prev != None):
                prev.next = temp
                return head
            else:
                return temp
        else:
            return head






a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)

# a3.next = a4
# a2.next = a3
a1.next = a2

sol = Solution()
h = sol.removeNthFromEnd(a1, 2)

while(h != None):
    print(h.val)
    h = h.next