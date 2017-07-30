# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        al = {}

        h = head
        while(h != None):
            val = h.val
            if(val in al):
                al[val] += 1
            else:
                al[val] = 1
            h = h.next


        ret = None
        retHead = None
        pointer = head
        while(pointer != None):
            val = pointer.val
            if(al[val] == 1):
                if(ret == None): 
                    ret = ListNode(pointer.val)
                    retHead = ret
                else:
                    ret.next = ListNode(pointer.val)
                    ret = ret.next
            pointer = pointer.next
        return retHead

                
a1 = ListNode(1)
a2 = ListNode(3)
a3 = ListNode(3)
a4 = ListNode(4)

a3.next = a4
a2.next = a3
a1.next = a2

a = Solution()
k = a.deleteDuplicates(None)

h = k
while(h!=None):
    print(h.val)
    h = h.next