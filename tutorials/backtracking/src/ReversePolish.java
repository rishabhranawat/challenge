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

    public List<List<Integer>> threeSum2(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();

        Integer a;
        Integer b;
        Integer c;

        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            a = nums[i];
            int start = i + 1;
            int end = nums.length - 1;
            while (start < end) {
                b = nums[start];
                c = nums[end];

                if (a + b + c == 0) {
                    Integer[] works = {a, b, c};
                    if(!list.contains(Arrays.asList(works))) list.add(Arrays.asList(works));
                    start += 1;
                    end -= 1;
                } else if (a + b + c > 0) {
                    end -= 1;
                } else {
                    start += 1;
                }
            }
        }
        return list;
    }

    public static void main(String[] args){
        ReversePolish s = new ReversePolish();
        int[] nums = {-2,0,1,1,2};
        System.out.println(s.threeSum2(nums));
    }
}