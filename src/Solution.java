import sun.jvm.hotspot.jdi.ArrayReferenceImpl;

import java.util.*;

class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> quarts = new LinkedList<>();
        quarts.size();
        for(int i = 0; i < nums.length - 3; i++){
            if(i == 0 || (i > 0 && nums[i] != nums[i-1])){
                for(int j = i+1; j < nums.length - 2; j++){
                    if(j == i+1 || (j > i+1 && nums[j] != nums[j-1])){
                        int high = nums.length - 1;
                        int low = j + 1;
                        while(high > low){
                            int tots = nums[high] + nums[low] + nums[j]+nums[i];
                            if(tots == target){
                                System.out.println(tots);
                                quarts.add(Arrays.asList(nums[i], nums[j], nums[low], nums[high]));
                                while(low < high && nums[low] == nums[low+1]) low += 1;
                                while(high > low && nums[high] == nums[high-1]) high -= 1;
                                high -= 1; low += 1;
                            }
                            else if(tots < target){
                                low += 1;
                            } else{
                                high -= 1;
                            }
                        }
                    }
                }
            }
        }
        return quarts;
    }

    public static void main(String[] args){
        Solution s = new Solution();
        int[] p = {1,0,-1,0,-2,2};
        System.out.println(s.fourSum(p, 0));
    }
}