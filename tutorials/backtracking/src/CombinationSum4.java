/**
 * Created by rishabh on 15/07/17.
 */
import java.util.*;
public class CombinationSum4 {

        public int combinationSum4(int[] nums, int target) {
            List<List<Integer>> list = new ArrayList<>();
            Arrays.sort(nums);
            backtrack(list, new ArrayList<>(), nums, target, 0, target);
            return list.size();
        }

        public void backtrack(List<List<Integer>> list, List<Integer> tempList, int[] nums, int remain, int level, int target){
            if(remain < 0) return;
            else if(remain == 0) {
                list.add(new ArrayList<>(tempList));
                int[] ns = new int[tempList.size()];
                for(int i = 0; i < tempList.size(); i++){
                    ns[i]  = tempList.get(i);
                }
                System.out.println(combinationSum4(ns, target));
            }
            else{
                for(int i = level; i < nums.length; i++){
                    tempList.add(nums[i]);
                    backtrack(list, tempList, nums, remain - nums[i], i, target);
                    tempList.remove(tempList.size()-1);
                }
            }
        }

        public static void main(String[] args){
            CombinationSum4 cs = new CombinationSum4();
            int[] s = {1,2,3};
            System.out.println(cs.combinationSum4(s, 4));
        }
}
