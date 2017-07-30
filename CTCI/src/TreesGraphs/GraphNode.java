package TreesGraphs;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by rishabh on 29/07/17.
 */
public class GraphNode{
    Integer val;
    List<GraphNode> adjacent;
    RouteBetweenNodes.State state;
    BuildOrder.State st;

    public GraphNode(int val){
        this.val = val;
        this.adjacent = new ArrayList<>();
    }

    public String toString(){
        return val.toString();
    }
}