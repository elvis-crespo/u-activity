package actividad2.BinaryTree;

// import actividad2.BinaryTree;
// import actividad2.Node;

public class App {
    public static void main(String[] args) {
        
        long startTime = System.currentTimeMillis();

        // create an object of BinaryTree
        BinaryTree tree = new BinaryTree();

        // create nodes of the tree
        tree.root = new Node(1);
        tree.root.left = new Node(2);
        tree.root.right = new Node(3);
        tree.root.left.left = new Node(4);

        System.out.print("\nBinary Tree: ");
        tree.traverseTree(tree.root);

        long endTime = System.currentTimeMillis();

        long executionTime = endTime - startTime;
        
        System.out.println("\nTiempo de ejecución: " + executionTime + " ms");
    
    }

}
