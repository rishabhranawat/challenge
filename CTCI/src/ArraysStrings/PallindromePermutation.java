package ArraysStrings;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by rishabh on 05/08/17.
 */
public class PallindromePermutation {
    public boolean palliPermu(String s){
        HashMap<Character, Integer> map = new HashMap<>();
        char[] arr = s.toCharArray();

        for(int i = 0; i < arr.length; i++){
            char val = arr[i];
            if(map.containsKey(val)) map.put(val, map.get(val)+1);
            else map.put(val, 1);
        }

        int odds = 0;
        int evens = 0;

        for(Map.Entry pairs: map.entrySet()){
            int val = (int) pairs.getValue();
            if(val % 2 != 0) odds += 1;
        }

        if(s.length() % 2 == 0) return odds == 2;
        else return odds == 1;
    }

    public static void main(String[] args){
        PallindromePermutation p = new PallindromePermutation();

        String s = "mo";
        System.out.println(p.palliPermu(s));
    }
}
