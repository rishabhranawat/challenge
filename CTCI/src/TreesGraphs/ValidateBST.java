package TreesGraphs;

/**
 * Created by rishabh on 30/07/17.
 */
public class ValidateBST {
    public boolean validateBST(TreeNode node, Integer min, Integer max){
        if(node == null) return true;
        if((min != null && node.val <= min) || (max != null && node.val >= max)) return false;
        return validateBST(node.left, min, node.val) && validateBST(node.right, node.val, max);

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

        TreeNode b = new TreeNode(20);
        TreeNode a = new TreeNode(10);
        TreeNode c = new TreeNode(30);
        TreeNode aa = new TreeNode(1);
        TreeNode ac = new TreeNode(25);
//
        a.left = aa;
        a.right = ac;

        b.left = a;
        b.right = c;




        ValidateBST v = new ValidateBST();
        System.out.println(v.validateBST(b, null, null));

    }
}
