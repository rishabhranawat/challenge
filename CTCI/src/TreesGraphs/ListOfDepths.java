package TreesGraphs;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Created by rishabh on 30/07/17.
 */
public class ListOfDepths {
    public List<List<TreeNode>> listOfDepths(TreeNode root){
        List<List<TreeNode>> ld = new ArrayList<>();

        Queue<TreeNode> currentLevel = new LinkedList<>();
        Queue<TreeNode> nextLevel = new LinkedList<>();

        currentLevel.add(root);
        ld.add(new LinkedList<>(currentLevel));
        while(!currentLevel.isEmpty() || !nextLevel.isEmpty()){
            if(currentLevel.isEmpty()){
                List<TreeNode> ad = new ArrayList<>(nextLevel);
                ld.add(ad);
                currentLevel = new LinkedList<>(nextLevel);
                nextLevel = new LinkedList<>();
            }
            TreeNode currNode = currentLevel.remove();
            if(currNode.left != null) nextLevel.add(currNode.left);
            if(currNode.right != null) nextLevel.add(currNode.right);

        }
        return ld;
    }

    public static void main(String[] args){
        TreeNode seven = new TreeNode(7);
        TreeNode eight = new TreeNode(8);
        TreeNode nine = new TreeNode(9);
        TreeNode ten = new TreeNode(10);
        TreeNode eleven = new TreeNode(11);
        TreeNode twel = new TreeNode(12);
        TreeNode thirt = new TreeNode(13);

        eight.left = ten;


        nine.left = twel;
        nine.right = thirt;

        seven.left = eight;
        seven.right = nine;


        ListOfDepths l = new ListOfDepths();
        System.out.println(l.listOfDepths(seven));

    }
}
