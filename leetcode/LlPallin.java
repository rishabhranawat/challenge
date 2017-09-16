import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

class LlPallin {
    public Integer getLength(ListNode head){
        Integer l = 0;
        while(head != null){
            l += 1;
            head = head.next;
        }
        return l;
    }
    
    public boolean isPalindrome(ListNode head) {
        Stack<Integer> stack = new Stack<>();

        int len = getLength(head);
        
        ListNode slow = head;
        ListNode fast = head;
        
        while(fast != null && fast.next != null){
            fast = fast.next.next;
            stack.add(slow.val);
            slow = slow.next;
        }

        if(len %2 != 0) slow = slow.next;
        while(!stack.isEmpty()){
            if(stack.pop() != slow.val) return false;
            slow = slow.next;
        }
        return true;
        
    }

    public static void main(String[] args){
        LlPallin l = new LlPallin();
        ListNode l1 = new ListNode(1);
        ListNode l2 = new ListNode(2);
        ListNode l3 = new ListNode(3);
        ListNode l4 = new ListNode(2);
        ListNode l5 = new ListNode(1);
        l4.next = l5;
        l3.next = l4;
        l2.next = l3;
        l1.next = l2;
        System.out.println(l.isPalindrome(l1));
    }
}