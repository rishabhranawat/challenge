# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if(head == None): return
        nodes = []
        h = head
        while(h != None):
            nodes.append(h)
            h = h.next
        
        start = 0 
        end = len(nodes)-1
        while(start < end):
            startNode = nodes[start]
            endNode = nodes[end]
            startNode.next = endNode
            endNode.next = nodes[start+1]
            start += 1
            end -= 1
        nodes[len(nodes)/2].next = None
    

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)

a3.next = a4
a2.next = a3
a1.next = a2

a = Solution()
k = a.reorderList(None)

h = a1
while(h!=None):
    print(h.val)
    h = h.next