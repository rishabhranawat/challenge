import java.util.HashMap;
import java.util.Map;

class Solution {
    public int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
        Map<Integer, Integer> pairSum = new HashMap<>();

        for(int i = 0; i < C.length; i++){
            for(int j = 0; j < D.length; j++){
                int tots = C[i]+D[j];
                pairSum.put(tots, pairSum.getOrDefault(tots, 0)+1);
            }
        }

        int counts = 0;
        for(int i = 0; i < A.length; i++){
            for(int j = 0; j < B.length; j++){
                counts += pairSum.getOrDefault(-1*(A[i]+B[j]), 0);
            }
        }
        return counts;
    }
}