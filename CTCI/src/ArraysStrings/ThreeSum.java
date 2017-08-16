package ArraysStrings;

import java.util.*;
/**
 * Created by rishabh on 12/08/17.
 */
public class ThreeSum {
    public List<List<Integer>> twoSum(int[] nums, int twoSum){
        List<List<Integer>> li = new ArrayList<>();
        HashMap<Integer, Integer> complementsIndex = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            complementsIndex.put(nums[i] - twoSum, i);
        }
        return null;
    }


    public List<List<Integer>> threeSum(int[] nums){
        List<List<Integer>> list = new ArrayList<>();

        Integer a;
        Integer b;
        Integer c;

        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            a = nums[i];
        }
        return list;
    }
}
