# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverse(self, x):
        for i in range(len(x)-1, -1, -1):
            this = x[i]
            if(i-1 == -1): this.next = None
            else:this.next = x[i-1]
        return x
            
    
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        s = []
        h = head
        start = None
        
        counter= 0
        retNode = None
        retHead = None
        while(h != None):
            if(counter >=m and counter < n):
                s.append(h)
            elif(counter == n):
                nodes = self.reverse(s)
            
            if(retNode == None):
                retNode = h
                retHead = h
            else:
                
                retNode.next = h
                retNode = retNode.next
            counter += 1
            h = h.next
        return retHead                
   

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


a = Solution()
h = a.reverseBetween(a1, 2, 4)


while(h != None):
    print(h.val)
    h = h.next

