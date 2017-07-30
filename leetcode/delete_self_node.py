# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def deleteNode(self, node):
		"""
		:type node: ListNode
		:rtype: void Do not return anything, modify node in-place instead.
		"""
		head = node
		prev = None
		while(head != None):
			if(head.next == None):
				prev.next = None
				break
			head.val = head.next.val
			prev = head
			head = head.next

		h = node
		while(h != None):
			print(h.val)
			h = h.next
            

           
a = ListNode(0)
b = ListNode(1)
c = ListNode(3)
d = ListNode(4)
b.next = c
a.next = b
c.next = d
sol = Solution()
sol.deleteNode(c)

# 0->1->3
# head.val = head.next.val
# head = head.next
# 1->1->3
# head.val = head.next.val
# head = head.next
# 1->3->3
# head.