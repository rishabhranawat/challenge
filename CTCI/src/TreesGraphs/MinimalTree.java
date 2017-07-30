package TreesGraphs;

import java.util.List;

/**
 * Created by rishabh on 30/07/17.
 */
public class MinimalTree {

    public TreeNode minimalTree(int[] vals, int start, int end){
        if(start > end) return null;
        Integer mid = (start+end)/2;
        TreeNode n = new TreeNode(vals[mid]);
        n.left = minimalTree(vals, start, mid-1);
        n.right = minimalTree(vals, mid+1, end);
        return n;
    }

    public void inOrder(TreeNode node){
        if(node != null){
            inOrder(node.left);
            System.out.println(node);
            inOrder(node.right);
        }
    }

    public static void main(String[] args){
        MinimalTree mt = new MinimalTree();
        int[] s = {0, 1, 2, 3, 4, 5, 6};
        TreeNode root = mt.minimalTree(s, 0, s.length-1);
        mt.inOrder(root);
    }
}
