package TreesGraphs;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by rishabh on 30/07/17.
 */
public class CheckBalanced {
    public Integer getHeight(TreeNode root){
        if(root == null) return 1;
        return 1 + Integer.max(getHeight(root.left), getHeight(root.right));
    }

    public boolean checkBalanced(TreeNode root){
        ListOfDepths l = new ListOfDepths();
        List<List<TreeNode>> lds = l.listOfDepths(root);

        for(List<TreeNode> level : lds){
            Integer d = null;
            for(TreeNode node: level){
                Integer h = getHeight(node);
                if(d == null) d = h;
                else if(h - d > 1) return false;
            }
        }
        return true;
    }

    public static void main(String[] args){
        TreeNode seven = new TreeNode(7);
        TreeNode eight = new TreeNode(8);
        TreeNode nine = new TreeNode(9);
        TreeNode ten = new TreeNode(10);
        TreeNode eleven = new TreeNode(11);
        TreeNode twel = new TreeNode(12);
        TreeNode thirt = new TreeNode(13);

        thirt.left = eleven;
        nine.left = twel;
        nine.right = thirt;


        seven.left = eight;
        seven.right = nine;

        CheckBalanced c = new CheckBalanced();
        System.out.println(c.checkBalanced(seven));
    }
}
