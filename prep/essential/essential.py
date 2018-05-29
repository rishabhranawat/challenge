def reverse(s):
	start = 0
	end = len(s)-1
	s = list(s)
	while(start < end):
		temp = s[start]
		s[start] = s[end]
		s[end] = temp
		start += 1
		end -= 1
	return "".join(s)

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def reverseLL(head):
	prev = None
	
	while(head != None):
		temp = head.next
		head.next = prev
		prev = head
		head = temp

	h = prev
	while(h):
		h = h.next
	return head

a = reverse("hey !!aa rishabh")
print(a)


n = Node(1)
n2 = Node(2)
n3 = Node(4)
n4 = Node(5)

n3.next = n4
n2.next = n3
n.next = n2

reverseLL(n)

