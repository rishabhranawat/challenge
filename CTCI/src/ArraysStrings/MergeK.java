package ArraysStrings;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

/**
 * Created by rishabh on 18/09/17.
 */

class MergeNode{
    int val;
    MergeNode next;

    public MergeNode(int val){
        this.val = val;
    }

    public String toString(){
        return "MergeNode: "+this.val;
    }
}
public class MergeK {

    public void mergeKLists(List<MergeNode> lists) {


    }

    public static void main(String[] args){
        List<MergeNode> l1 = new ArrayList<>();
        l1.add(new MergeNode(100));
        l1.add(new MergeNode(15));
        l1.add(new MergeNode(17));

        List<MergeNode> l2 = new ArrayList<>();
        l2.add(new MergeNode(1));
        l2.add(new MergeNode(16));
        l2.add(new MergeNode(18));

        List<List<MergeNode>> lists= new ArrayList<>();
        lists.add(l1);
        lists.add(l2);

        MergeK mk = new MergeK();

        int[]x = {123};
        int a = x.length;

        PriorityQueue<MergeNode> queue = new PriorityQueue<>(3,
                new Comparator<MergeNode>() {
                    @Override
                    public int compare(MergeNode o1, MergeNode o2) {
                        if(o1.val < o2.val) return -1;
                        else if(o1.val == o2.val) return 0;
                        else return 1;
                    }
                });

        for (MergeNode m:l1){
            queue.add(m);
        }
        while(!queue.isEmpty()){
            System.out.println(queue.poll());
        }
        System.out.println(queue);

    }

}
