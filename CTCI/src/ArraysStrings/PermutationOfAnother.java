package ArraysStrings;

import java.util.HashMap;

/**
 * Created by rishabh on 05/08/17.
 */
public class PermutationOfAnother {
    public boolean isPermutation(String s1, String s2){
        if(s1 == null || s2 == null) return false;
        if(s1.length() != s2.length()) return false;

        HashMap<Character, Integer> s1Map = new HashMap<>();
        for(int i = 0; i < s1.length(); i++){
            Character val = s1.charAt(i);
            if(s1Map.containsKey(val)) s1Map.put(val, s1Map.get(val)+1);
            else s1Map.put(val, 1);
        }

        for(int i = 0; i < s2.length(); i++){
            Character val = s2.charAt(i);
            if(!s1Map.containsKey(val) || s1Map.get(val) == 0) return false;
            else s1Map.put(val, s1Map.get(val)-1);
        }
        return true;
    }

    public static void main(String[] args){
        PermutationOfAnother p = new PermutationOfAnother();
        String s1 = "hi hey";
        String s2 = "yeh yeh";
        System.out.println(p.isPermutation(s1, s2));
    }
}
