class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] aux = new int[nums.length];
        for(int i = 0; i < nums.length; i++){
            int mult = 1;
            for(int j = 0; j < nums.length; j++){
                if(i != j){
                    mult *= nums[j];
                }
            }
            aux[i] = mult;
        }
        return aux;
    }

    public static void main(String[] args){

        Solution s = new Solution();

        int[] input = new int[]{1, 2, 3, 4};
        int[] output = s.productExceptSelf(input);
        for(int i = 0; i < output.length; i++){
            System.out.println(output[i]);
        }
    }
} 