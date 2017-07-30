package TreesGraphs;

import java.util.*;

/**
 * Created by rishabh on 30/07/17.
 */
public class BuildOrder {

    enum State {Unvisited, Visited, Visiting};


    public void DFS(LinkedList<GraphNode> sorted, GraphNode startingNode){
        Stack<GraphNode> stackOfVisiting = new Stack<>();
        startingNode.st = State.Visiting;
        stackOfVisiting.push(startingNode);

        while(!stackOfVisiting.isEmpty()) {
            GraphNode visitingNode = stackOfVisiting.peek();
            visitingNode.st = State.Visiting;

            boolean unvisitedChildren = false;
            for (GraphNode adjNode : visitingNode.adjacent) {
                if (adjNode.st == State.Unvisited) {
                    System.out.println(adjNode);
                    stackOfVisiting.push(adjNode);
                    unvisitedChildren = true;
                    break;
                }
            }
            if (unvisitedChildren == false) {
                visitingNode.state = RouteBetweenNodes.State.Visited;
                sorted.add(visitingNode);
                stackOfVisiting.pop();
            }
        }

    }

    public List<GraphNode> topSort(Graph graph){
        LinkedList<GraphNode> inSortedOrder = new LinkedList<>();

        for(GraphNode graphNode: graph.nodes){
            graphNode.st = State.Unvisited;
        }

        for(GraphNode g: graph.nodes){
            if(g.st == State.Unvisited) DFS(inSortedOrder, g);
        }

        System.out.println(inSortedOrder);
        return inSortedOrder;
    }

    public static void main(String[] args){
//        GraphNode a = new GraphNode(1);
//        GraphNode b = new GraphNode(2);
//        GraphNode c = new GraphNode(3);
//        GraphNode d = new GraphNode(4);
//        GraphNode e = new GraphNode(5);
//        GraphNode f = new GraphNode(6);
//
//        d.adjacent.add(a);
//        b.adjacent.add(f);
//        d.adjacent.add(b);
//        a.adjacent.add(f);
//        c.adjacent.add(d);
//
//        GraphNode[] g = {a, b, c, d, e, f};
//        Graph graph = new Graph();
//        graph.nodes = Arrays.asList(g);
//
        BuildOrder n = new BuildOrder();
//        System.out.println(n.topSort(graph));


        GraphNode shirt = new GraphNode(1);
        GraphNode tie = new GraphNode(2);
        GraphNode jacket = new GraphNode(3);
        GraphNode belt = new GraphNode(4);
        GraphNode pants = new GraphNode(5);
        GraphNode undershorts = new GraphNode(6);
        GraphNode shoes = new GraphNode(7);
        GraphNode socks = new GraphNode(8);
        GraphNode watch = new GraphNode(9);


        tie.adjacent.add(jacket);
        belt.adjacent.add(jacket);

        shirt.adjacent.add(tie);
        shirt.adjacent.add(belt);

        pants.adjacent.add(belt);
        pants.adjacent.add(shoes);
        undershorts.adjacent.add(pants);
        undershorts.adjacent.add(shoes);
        socks.adjacent.add(shoes);

        GraphNode[] wear = {shirt, tie, jacket, belt, pants, undershorts, shoes, socks, watch};
        Graph wearGraph = new Graph();
        wearGraph.nodes = Arrays.asList(wear);

        System.out.println(n.topSort(wearGraph));


    }


}
