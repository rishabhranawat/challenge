package TreesGraphs;

/**
 * Created by rishabh on 30/07/17.
 */
public class TreeNode {
    Integer val;
    TreeNode left;
    TreeNode right;
    TreeNode parent;
    TreeNode next;

    public TreeNode(Integer val){
        this.val = val;
    }

    public String toString(){
        return this.val.toString();
    }
}
