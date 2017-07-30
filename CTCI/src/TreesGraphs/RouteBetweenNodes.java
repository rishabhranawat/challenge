package TreesGraphs;

import java.util.Arrays;
import java.util.Stack;

/**
 * Created by rishabh on 29/07/17.
 */
public class RouteBetweenNodes {
    enum State {Unvsited, Visited, Visiting};

    public boolean search(Graph graph, GraphNode start, GraphNode end){
        if(start == end) return true;

        // Mark all initially unvisited
        for(GraphNode graphNode:graph.nodes){
            graphNode.state = State.Unvsited;
        }

        Stack<GraphNode> stackOfVisiting = new Stack<>();
        GraphNode startingNode = start;
        startingNode.state = State.Visiting;
        System.out.println(startingNode);
        stackOfVisiting.push(startingNode);

        while(!stackOfVisiting.isEmpty()){
            GraphNode visitingNode = stackOfVisiting.peek();
            visitingNode.state = State.Visiting;

            boolean unvisitedChildren = false;
            for(GraphNode adjNode: visitingNode.adjacent){
                if(adjNode.state == State.Unvsited){
                    System.out.println(adjNode);
                    stackOfVisiting.push(adjNode);
                    if(end == adjNode) return true;
                    unvisitedChildren = true;
                    break;
                }
            }
            if(unvisitedChildren == false){
                visitingNode.state = State.Visited;
                stackOfVisiting.pop();
            }
        }
        return false;
    }

    public static void main(String[] args){
        GraphNode zero = new GraphNode(0);
        GraphNode one = new GraphNode(1);
        GraphNode three = new GraphNode(3);
        GraphNode four = new GraphNode(4);
        GraphNode five = new GraphNode(5);
        GraphNode two = new GraphNode(2);

        zero.adjacent.add(one);
        zero.adjacent.add(five);
        zero.adjacent.add(four);

        one.adjacent.add(three);
        one.adjacent.add(four);

        two.adjacent.add(one);

        three.adjacent.add(two);
        three.adjacent.add(four);

        Graph graph = new Graph();
        GraphNode[] graphNodes = {one, two, three, four, five};
        graph.nodes = Arrays.asList(graphNodes);

        RouteBetweenNodes route = new RouteBetweenNodes();
        System.out.println(route.search(graph, four, three));
    }
}
