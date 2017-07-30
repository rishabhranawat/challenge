import java.util.LinkedList;
import java.util.Queue;

public class MyStack {

    Queue<Integer> qs;

    /** Initialize your data structure here. */
    public MyStack() {
        this.qs = new LinkedList<>();
    }

    /** Push element x onto stack. */
    public void push(int x) {
        this.qs.add(x);
        for(int i = 0; i < this.qs.size()-1; i++){
            this.qs.add(this.qs.poll());
        }
    }

    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        return this.qs.poll();
    }

    /** Get the top element. */
    public int top() {
        return this.qs.peek();
    }

    /** Returns whether the stack is empty. */
    public boolean empty() {
        return this.qs.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */