/**
 * Created by rishabh on 15/07/17.
 */
import java.util.*;

public class CombinationSum {
    public List<List<Integer>> combinationSums(int[] nums, int target){
        List<List<Integer>> list = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(list, new ArrayList<>(), nums, target, 0);
        return list;
    }

    public void backtrack(List<List<Integer>> list, List<Integer> tempList, int[] nums, int remain, int start){
        if(remain < 0) return;
        else if(remain == 0) list.add(new ArrayList<>(tempList));
        else{
            for(int i = start; i < nums.length; i++){
                tempList.add(nums[i]);
                backtrack(list, tempList, nums, remain - nums[i], i);
                tempList.remove(tempList.size()-1);
            }
        }
    }

    public static void main(String[] args){
        CombinationSum cs = new CombinationSum();
        int[] s = {2, 3, 6, 4, 7};
        System.out.println(cs.combinationSums(s, 7));
    }

}
