/**
 * Created by rishabh on 15/07/17.
 */
import java.util.*;

public class CombinationSum3 {
    public List<List<Integer>> combinationSum3(int k, int n) {
        int[] nums = new int[9];
        for(int i =0; i < 9; i++){
            nums[i] = i+1;
        }
        List<List<Integer>> list = new ArrayList<>();
        backtrack(list, new ArrayList<>(), nums, k, n, 0);
        return list;
    }

    public void backtrack(List<List<Integer>> list, List<Integer> tempList, int[] nums, int k, int remain, int level){
        if(remain < 0) return;
        else if(remain == 0 && tempList.size() == k){
            list.add(new ArrayList<>(tempList));
        } else {
            for(int i = level; i < nums.length; i++){
                tempList.add(nums[i]);
                backtrack(list, tempList, nums, k, remain-nums[i], i+1);
                tempList.remove(tempList.size()-1);
            }
        }
    }

}
