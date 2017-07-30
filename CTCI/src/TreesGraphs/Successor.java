package TreesGraphs;

/**
 * Created by rishabh on 30/07/17.
 */
public class Successor {

    public TreeNode leftMostChild(TreeNode node){
        TreeNode head = node;
        while(head.left != null){
            head = head.left;
        }
        return head;
    }

    public TreeNode successor(TreeNode node){
        if(node.right != null){
            return leftMostChild(node.right);
        } else {
            TreeNode q = node.parent;
            TreeNode x = node;
            while(x != null && x.left != q){
                q = x;
                x = x.parent;
            }
            return x;
        }
    }
}
