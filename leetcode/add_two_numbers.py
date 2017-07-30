# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def getNumber(l):
    s = ""
    head = l
    while(head != None):
        s = str(head.val) + s
        head = head.next
    return s
def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    val = str(int(getNumber(l1)) + int(getNumber(l2)))
    k = len(val)-1
    n = ListNode(val[k])
    head = n
    for i in range(k-1, -1, -1):
        new = ListNode(val[i])
        head.next = new
        head = head.next
    return n

l1 = ListNode(2)
l1.next = (ListNode(4))
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

l = addTwoNumbers(l1, l2)
while(l != None):
    print(l.val)
    l = l.next