import java.util.*;

public class ReversePolish {

    public String[] k = {"/", "+", "-", "*"};
    public List<String> operations =  Arrays.asList(k);

    public boolean isOperation(String s){
        if(operations.contains(s)) return true;
        return false;
    }

    public Integer perform(String s, Integer total, Integer num2){
        if(s == "/") return num2/total;
        else if(s == "*") return total*num2;
        else if(s == "+") return total + num2;
        else return num2 - total;
    }

    public int evalRPN(String[] tokens) {
        Integer total = null;
        Queue<Integer> nums = new LinkedList<>();
        Queue<String> ops = new LinkedList<>();

        for(String exp: tokens){
            if(isOperation(exp)) ops.add(exp);
            else nums.add(Integer.parseInt(exp));
        }

        while(!nums.isEmpty()){
            int num2 = nums.poll();
            if(total == null){
                total = nums.poll();
            }
            total = perform(ops.poll(), total, num2);
        }
        return total;
    }

    public static void main(String[] args){
        String[] e =  {"4", "13", "5", "/", "+"};
        ReversePolish r = new ReversePolish();
        System.out.println(r.evalRPN(e));
    }
}