import java.util.ArrayList;
import java.util.List;

/**
 * Created by rishabh on 29/07/17.
 */
public class Heap {
    private List<Integer> heapArr;

    public Heap(){
        this.heapArr = new ArrayList<>();
        heapArr.add(7);
        heapArr.add(8);
        heapArr.add(20);
        heapArr.add(10);
        heapArr.add(11);
    }

    public int getLeft(int index){
        return (2*index)+1;
    }

    public int getRight(int index){
        return (2*index)+2;
    }

    public int getParent(int index){
        Double tempIndex = ((double)index-2)/2;
        return (int)Math.round(tempIndex);
    }

    public boolean insert(int child){
        this.heapArr.add(child);
        int childIndex = this.heapArr.size()-1;
        int parentIndex = getParent(childIndex);

        while(parentIndex >= 0){
            int parent = this.heapArr.get(parentIndex);
            System.out.println(parent+" "+child);
            if(parent > child){
                this.heapArr.set(parentIndex, child);
                this.heapArr.set(childIndex, parent);
                childIndex = parentIndex;
                parentIndex = getParent(childIndex);
            } else {
                break;
            }
        }
        return true;
    }

    public int extractMin(){

        int minVal = this.heapArr.get(0);
        int lastIndex = this.heapArr.size()-1;
        int lastValue = this.heapArr.get(lastIndex);

        int currentIndex = 0;
        this.heapArr.set(currentIndex, lastValue);

        this.heapArr.remove(lastIndex);

        int leftIndex = getLeft(currentIndex);
        int rightIndex = getRight(currentIndex);

        while(rightIndex < this.heapArr.size()){
            int leftVal = this.heapArr.get(leftIndex);
            int rightVal = this.heapArr.get(rightIndex);

            if(leftVal < lastValue && leftVal < rightVal){
                this.heapArr.set(currentIndex, leftVal);
                this.heapArr.set(leftIndex, lastValue);
                leftIndex = getLeft(leftIndex);
                rightIndex = getRight(leftIndex);
            } else if(rightVal < lastValue && rightVal < leftVal){
                this.heapArr.set(currentIndex, rightVal);
                this.heapArr.set(rightIndex, lastValue);
                leftIndex = getLeft(rightIndex);
                rightIndex = getRight(rightIndex);
            } else {
                break;
            }
        }
        return minVal;
    }

    public String toString(){
       return this.heapArr.toString();
    }

    public static void main(String[] args){
        Heap h = new Heap();
        System.out.println(h.toString());
        h.insert(5);
        System.out.println(h.toString());
        System.out.println(h.extractMin());

        System.out.println(h.toString());

    }

}
