package ArraysStrings;

import java.util.Arrays;
import java.util.HashSet;

/**
 * Created by rishabh on 05/08/17.
 */

/**
 * O(n) solution
 * O(n) extra space
 * You need an extra data structure. Even the book
 * uses an array of booleans.
 */
public class IsUnique {
    public boolean isUnique(String str){
        if(str == null) return true;
        HashSet<Character> s = new HashSet<>();
        for(int i = 0; i < str.length(); i++){
            if(s.contains(str.charAt(i))) return false;
            else s.add(str.charAt(i));
        }
        return true;
    }
    public static void main(String[] args){
        String str = null;
        IsUnique s = new IsUnique();
        System.out.println(s.isUnique(str));
    }
}
