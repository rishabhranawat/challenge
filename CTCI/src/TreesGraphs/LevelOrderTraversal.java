package TreesGraphs;

import java.util.*;


public class LevelOrderTraversal {

    public List<List<Integer>> levelOrder(TreeNode root) {


        if(root == null) return new ArrayList<>();

        Queue<TreeNode> currentLevel = new LinkedList<TreeNode>();
        Queue<TreeNode> nextLevel = new LinkedList<TreeNode>();

        List<List<Integer>> levelList = new ArrayList<>();
        currentLevel.add(root);

        List<Integer> currentVals = new ArrayList<>();
        while(!currentLevel.isEmpty()){
            TreeNode currentNode = currentLevel.remove();
            if(currentNode!= null) {
                currentVals.add(currentNode.val);
                nextLevel.add(currentNode.left);
                nextLevel.add(currentNode.right);
            }
            if(currentLevel.isEmpty()){
                if(currentVals.size()>0) levelList.add(new ArrayList<>(currentVals));
                currentVals = new ArrayList<>();
                currentLevel = new LinkedList<>(nextLevel);
                nextLevel = new LinkedList<>();
            }
        }
        return levelList;
    }
}