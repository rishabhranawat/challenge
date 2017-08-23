package LeetCode;

import java.util.*;

/**
 * Created by rishabh on 21/08/17.
 */
class Node{
    ArrayList<Node> children;
    char data;
    int id;

    public Node(int id, char data){
        children = new ArrayList<>();
        this.id = id;
        this.data =  data;
    }

    public String toString(){
        return("id: "+id+" children: "+children.size());
    }
}
public class NumberOfIslands {


    public HashMap<Integer, Node> convertToNodes(char[][] matrix){
        HashMap<Integer, Node> map = new HashMap<>();

        for(Integer i = 0; i < matrix.length; i++){
            for(Integer j = 0; j < matrix[i].length; j++){
                int id = Integer.parseInt(i.toString() + j.toString());
                Node n = new Node(id, matrix[i][j]);
                map.put(id, n);
            }
        }

        for(Integer i = 0; i < matrix.length; i++){
            for(Integer j = 0; j < matrix[i].length; j++){
                Node currNode = map.get(Integer.parseInt(i.toString()+j.toString()));
                if(currNode.data == '1') {
                    if (j + 1 < matrix[i].length) {
                        int id = Integer.parseInt(i.toString() + Integer.toString(j + 1));
                        if (matrix[i][j + 1] == '1') currNode.children.add(map.get(id));
                    }
                    if (i + 1 < matrix.length) {
                        int id = Integer.parseInt(Integer.toString(i + 1) + j.toString());
                        if (matrix[i + 1][j] == '1') currNode.children.add(map.get(id));
                    }
                    if(i - 1 >= 0){
                        int id = Integer.parseInt(Integer.toString(i - 1) + j.toString());
                        if (matrix[i - 1][j] == '1') currNode.children.add(map.get(id));
                    }
                    if(j - 1 >= 0){
                        int id = Integer.parseInt(Integer.toString(i) + Integer.toBinaryString(j-1));
                        if (matrix[i][j-1] == '1') currNode.children.add(map.get(id));

                    }
                }
            }
        }
        return map;
    }

    public int numIslands(char[][] matrix){
        Integer numOfNodes = 0;
        if(matrix.length == 0) return 0;
        HashMap<Integer, Node> map = convertToNodes(matrix);

        System.out.println(map);
        Set<Node> visited = new HashSet<>();

        for(Map.Entry<Integer, Node> pairs: map.entrySet()) {
            Node currNode = pairs.getValue();

            if (!visited.contains(currNode)) {

                Queue<Node> toBeVisited = new LinkedList<>();
                toBeVisited.add(currNode);
                System.out.println("NEW NODE"+currNode);

                while (!toBeVisited.isEmpty()) {
                    Node head = toBeVisited.remove();
                    head.children.stream().forEach(
                            c -> {
                                if (c != null && !toBeVisited.contains(c) && !visited.contains(c)){

                                    toBeVisited.add(c);
                                }
                            }
                    );
                    visited.add(head);
                }
                if(currNode.data == '1'){
                    numOfNodes += 1;
                }
            }
        }
        return numOfNodes;
    }


    public static void main(String[] args){
        NumberOfIslands numberOfIslands = new NumberOfIslands();

        char[][] matrix2 = {{'1', '0', '1', '1', '0', '1', '1'}};
        char[][] matrix3 = {"111111111111111001111111111111111111111111000011111111111111111111111111111111111111".toCharArray()};
        System.out.println(numberOfIslands.numIslands(matrix3));
    }
}