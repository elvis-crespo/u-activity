package actividad2.LinkedList;

import actividad2.LinkedList.LinkedList.Node;

public class App {
    public static void main(String[] args) {

        long startTime = System.currentTimeMillis();
        // create an object of LinkedList
        LinkedList linkedList = new LinkedList();
        
        // assign values to each linked list node
        linkedList.head = new Node(1);
        Node second = new Node(2);
        Node third = new Node(3);
        
        // connect each node of linked list to next node
        linkedList.head.next = second;
        second.next = third;
        
        // printing node-value
        System.out.print("LinkedList: ");
        while (linkedList.head != null) {
            System.out.print(linkedList.head.value + " ");
            linkedList.head = linkedList.head.next;
        }
        
        long endTime = System.currentTimeMillis();
        long executionTime = endTime - startTime;
        
        System.out.println("\nTiempo de ejecución: " + executionTime + " ms");
    }
}
