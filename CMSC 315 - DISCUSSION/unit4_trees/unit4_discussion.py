"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """

        """inderting depends on comparing the current node to the value due to the BST rule: smaller left and larger 
        right childern.each comparson directs use the subtree the value belongs in, in turn also cutting the search
        time nessary going from linearly checking all values O(n) to balanced binary O(log n)."""

        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """

        if node is None:
            return Node(value)
        if value < node.value:
            #smaller values stay on the left to keep the order
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            #larger vakues stay o the right
            node.right = self._insert_recursive(node.right, value)
        return node


    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        """
        BST search is often faster than linear search because each
        comparison throws away an entire subtree. A linear search on a
        list checks items one by one, which is O(n). In a balanced BST,
        every step roughly halves the remaining values, so search takes
        about O(log n) steps. (In a badly unbalanced tree, such as one
        built from already sorted data, it can degrade to O(n).)
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            #value is smaller so it can only be in the left tree
            return self._search_recursive(node.left, value)
        #value is larger so it can only be in the right tree
        return self._search_recursive(node.right, value)


    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        """
        In-order traversal goes left subtree to node, node to right subtree. Since left is smaller than node and right is larger than node
        this traversals visits smallest to largest, producing a sorted output.
        """
        if node is None:
            return
        self._inorder_recursive(node.left, values)  # smaller value
        values.append(node.value)                   # then current node
        self._inorder_recursive(node.right, values) # then larger value


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.


    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    redwood = BST()
    startingValues = [50, 30, 70, 20, 40, 40, 60, 80]

    for i in startingValues:
        redwood.insert(i)
    print("values inserted: ", startingValues)
    # Each insert compares against existing nodes and goes only one way
    # at each level, so the search space for its position shrinks every step

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    print("TODO: Display and explain traversal results.")
    ioTraversal = redwood.inorder()
    print( "ascending order of values:", ioTraversal)
    # values were inserted out of order, but the output is sorted.
    # In-order goes from the left (smaller), to node, to right (larger) at every level,
    # so the BST ordering rule guarantees ascending output.
    print( "sorted correctly?", ioTraversal == sorted(ioTraversal))

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")
    
    # 40 exists: 40 < 50 go left, 40 > 30 go right, found. 3 comparisons.
    print("Search 40:", redwood.search(40))
    # 80 exists: 80 > 50 right, 80 > 70 right, found. 3 comparisons.
    print("Search 80:", redwood.search(80))
    # 65 does not exist: 65 > 50 right, 65 < 70 left, 65 > 60 right -> empty, False.
    print("Search 65:", redwood.search(65))
    # 10 does not exist: 10 < 50 left, 10 < 30 left, 10 < 20 left -> empty, False.
    print("Search 10:", redwood.search(10))
    # Every search, hit or miss, took at most 3 comparisons out of 7 values,
    # where a linear search could need all 7.
    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    print("---Empty tree traversal---")
    empty = BST()
    # Traversing and searching empty tree
    print("Empty tree traversal:", empty.inorder()) #returns empty list
    print("(Empty) search: 5", empty.search(5)) # returns False
    
    # Duplicate values
    print("--- Duplicate entry test---")
    redwood.insert(65)
    print("After inserting 65 (Duplicate entry)", redwood.inorder())
    
    # BST with one node, where node is lso a leaf node. traversal just returns tha single value,
    # and searching that node finds one comparison
    print("---Single node traversal and serach---")
    one_node = BST() # initializing empty BST
    one_node.insert(44) #inserting a single node into the tree
    print("Single node traversal", one_node.inorder()) # sorting the values in th tree
    print ("Single node search: 44", one_node.search(44)) # searching for value 44 in the BST

if __name__ == "__main__":
    main()