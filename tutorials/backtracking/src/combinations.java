/**
 * Created by rishabh on 15/07/17.
 */

import java.util.*;
public class combinations {
    public List<List<Integer>> getCombinations(int n, int k){
        int[] nums = new int[n];
        for(int i =0; i < n; i++){
            nums[i] = i+1;
        }
        List<List<Integer>> list = new ArrayList<>();
        backtrack(list, new ArrayList<>(), nums, k, 0);
        return list;
    }

    public void backtrack(List<List<Integer>> list, List<Integer> tempList, int[] nums, int k, int level){
        if(tempList.size() == k) list.add(new ArrayList<>(tempList));
        else{
            for(int i = level; i<nums.length; i++){
                tempList.add(nums[i]);
                backtrack(list, tempList, nums, k, i+1);
                tempList.remove(tempList.size()-1);
            }
        }
    }

    public static void main(String[] args){
        combinations c = new combinations();
        System.out.println(c.getCombinations(4, 2));
    }

}
