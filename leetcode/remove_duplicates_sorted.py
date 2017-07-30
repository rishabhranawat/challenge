class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if(head == None): return
    current_val = head.val
    current_node = head
    while(head != None):
        if(current_val != head.val):
            current_val = head.val
            current_node.next = head
            current_node = head
        head = head.next


n1 = ListNode(1)

deleteDuplicates(n1)

head = n1
while(head != None):
    print(head.val)
    head = head.next