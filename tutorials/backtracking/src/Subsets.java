import java.util.*;

public class Subsets{
	public List<List<Integer>> subsets(int[] nums){
		List<List<Integer>> list = new ArrayList<>();
		Arrays.sort(nums);
		backtrack(list, new ArrayList<>(), nums, 0);
		return list;
	}

	public void backtrack(List<List<Integer>> list, List<Integer> tempList, int[] nums, int start){
		list.add(new ArrayList<>(tempList));
		for(int i = start; i < nums.length; i++){
			tempList.add(nums[i]);
			backtrack(list, tempList, nums, i+1);
			System.out.println(tempList);
			tempList.remove(tempList.size()-1);
		}
	}
	public static void main(String[] args){
		Subsets sub = new Subsets();
		int[] s = {1, 2, 3, 3};
		System.out.println(sub.subsets(s));
	}
}