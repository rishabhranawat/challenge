package TreesGraphs;
import java.util.*;

public class LowestCommonAncestorBT {
    public boolean onPath(TreeNode root, TreeNode p){
        if(root == null) return false;
        else if(root == p) return true;
        return onPath(root.left, p) || onPath(root.right, p);
    }

    public TreeNode getLCA(TreeNode root, TreeNode p, TreeNode q){
        if(root == null) return null;
        else if(root == p) return p;
        else if(root == q) return q;

        boolean val1 = onPath(root.left, p);
        if(val1 != onPath(root.left, q)) return root;
        else{
            TreeNode currNode = val1 ? root.left:root.right;
            return getLCA(currNode, p, q);
        }
    }

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root != null && p != null && q != null){
            if(!onPath(root, p) || !onPath(root, q)) return null;
            else return getLCA(root, p, q);
        }
        return null;
    }
}