import java.util.Arrays;

/**
 * Created by rishabh on 29/11/17.
 */
public class MatrixMult {
    public static int[][] transp(int[][] a){
        int[][] ret = new int[a.length][a[0].length];
        for(int i = 0; i < a.length; i++){
            for(int j = 0; j < a[0].length; j++){
                ret[j][i] = a[i][j];
            }
        }
        return ret;
    }

    public static int[][] mult(int[][] a, int[][] b){



        int[][] ret = new int[a[0].length][b[0].length];

        for(int row = 0; row < a.length; row++){
            int[] r = a[row];
            for(int col = 0; col < b.length; col++){
                int[] c = b[col];
                System.out.println(Arrays.toString(r));
                System.out.println(Arrays.toString(c));
            }
        }

        return null;
    }

    public static void main(String[] args){
        int[][] a = {{1, 2}, {3, 4}};
        int[][] b = {{5, 6},{7, 8} };

        System.out.println(mult(a, transp(b)));
    }
}
