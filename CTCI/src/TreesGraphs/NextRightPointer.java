package TreesGraphs;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Created by rishabh on 15/08/17.
 */
public class NextRightPointer {
    public void connect(TreeNode root) {
        List<List<TreeNode>> levels = levelOrder(root);
        for(List<TreeNode> level: levels){
            for(int i = 0; i < level.size(); i++){
                if(i == level.size()-1){
                    level.get(i).next = null;
                } else {
                    level.get(i).next = level.get(i+1);
                }
            }
        }
    }

    public List<List<TreeNode>> levelOrder(TreeNode root) {

        if(root == null) return new ArrayList<>();

        Queue<TreeNode> currentLevel = new LinkedList<TreeNode>();
        Queue<TreeNode> nextLevel = new LinkedList<TreeNode>();

        List<List<TreeNode>> levelList = new ArrayList<>();
        currentLevel.add(root);

        List<TreeNode> currentVals = new ArrayList<>();
        while(!currentLevel.isEmpty()){
            TreeNode currentNode = currentLevel.remove();
            if(currentNode!= null) {
                currentVals.add(currentNode);
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
