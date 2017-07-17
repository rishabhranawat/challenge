// Backtracking solution to 3 Sum
public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(list, new ArrayList<>(), nums, 0, 0);
        return list;
    }
    
    public void backtrack(List<List<Integer>> list, List<Integer> tempList, int[] nums, int tots, int level){
        if(tempList.size() == 3 && tots == 0 && !list.contains(tempList)) list.add(new ArrayList<>(tempList));
        else{
            for(int i = level; i < nums.length; i++){
                tempList.add(nums[i]);
                backtrack(list, tempList, nums, tots+nums[i], i+1);
                tempList.remove(tempList.size()-1);
            }
        }
    }

public class Solution {
//     public List<List<Integer>> threeSum(int[] nums) {
//         List<List<Integer>> list = new ArrayList<>();
//         Arrays.sort(nums);
//         backtrack(list, new ArrayList<>(), nums, 0, 0);
//         return list;
//     }
    
//     public void backtrack(List<List<Integer>> list, List<Integer> tempList, int[] nums, int tots, int level){
//         if(tempList.size() == 3 && tots == 0 && !list.contains(tempList)) list.add(new ArrayList<>(tempList));
//         else{
//             for(int i = level; i < nums.length; i++){
//                 tempList.add(nums[i]);
//                 backtrack(list, tempList, nums, tots+nums[i], i+1);
//                 tempList.remove(tempList.size()-1);
//             }
//         }
//     }
    
    public List<List<Integer>> threeSum(int[] nums){
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
                    while(start < end && nums[start] == nums[start + 1]) start += 1;
                    while(start < end && nums[end]== nums[end-1]) end -= 1;
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
}
}
