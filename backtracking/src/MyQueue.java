import java.util.Stack;

public class MyQueue {

    Stack<Integer> sq;
    /** Initialize your data structure here. */
    public MyQueue() {
        this.sq = new Stack<>();
    }

    /** Push element x to the back of queue. */
    public void push(int x) {
        for(int i = 0; i < this.sq.size()-1; i ++){
            this.sq.push(this.sq.pop());
        }
        this.sq.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
       return this.sq.pop();
    }

    /** Get the front element. */
    public int peek() {
        return this.sq.firstElement();
    }

    /** Returns whether the queue is empty. */
    public boolean empty() {
        return this.sq.empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */