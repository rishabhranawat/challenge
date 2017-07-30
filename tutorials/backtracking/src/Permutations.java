/**
 * Created by rishabh on 15/07/17.
 */

import java.util.*;
public class Permutations {

    public List<List<Integer>> permutations(int[] nums){
        List<List<Integer>> list = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(list, new ArrayList<>(), nums, 0);
        return list;
    }

    public void backtrack(List<List<Integer>> list, List<Integer> tempList, int[] nums, int level){
        if(tempList.size() == nums.length) list.add(new ArrayList<>(tempList));
        else{
            for(int i = level; i < nums.length; i++){
                if(tempList.contains(nums[i])) continue;;
                tempList.add(nums[i]);
                backtrack(list, tempList, nums, i+1);
                tempList.remove(tempList.size()-1);
            }
        }
    }
}
