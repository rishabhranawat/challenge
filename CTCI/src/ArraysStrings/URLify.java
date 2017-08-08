package ArraysStrings;

import java.util.Arrays;

/**
 * Created by rishabh on 05/08/17.
 */
public class URLify {
    public String urlify(String str, int length){
        int space = 0;
        char[] arr = str.toCharArray();
        for(int i = 0; i < length; i++){
            if(arr[i] == ' ') space += 1;
        }
        int newLength = space*2 + length;
        for(int j = length-1; j >= 0; j--){
            if(arr[j] == ' '){
                arr[newLength - 3] = '%';
                arr[newLength - 2] = '2';
                arr[newLength - 1] = '0';
                newLength -= 3;
            } else {
                arr[newLength - 1] = arr[j];
                newLength -= 1;
            }
        }
        return String.copyValueOf(arr);
    }

    public static void main(String[] args){
        URLify u = new URLify();
        System.out.println(u.urlify("Mr John Smith    ",13));
    }
}
