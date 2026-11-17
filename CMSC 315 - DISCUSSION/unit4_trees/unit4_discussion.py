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
        self.value = value  #the data  this node holds
        self.left = None    # Reference the left child (initially none)
        self.right = None   # Reference th right child (initially None)


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None    # empty tree

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
        # start at the root, the helper method returns it back so it can be stored.
        # if root is none, helper creates the first node and returns it
        self.root = self._insert_recursive(self.root, value)

        # insertion compares the value to each node so it goes left when smaller and right when larger,
        # which keeps the BST ordering rule true and lets searches skip half the tree at each step.

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
        # create new node and give it to the parent node
        if node is None:
            return Node(value)
        # to obey BST rules: the nodes left subtree is larger than it and the nodes
        # right subtree is larger than it. if the new value is larger or smaller tells it which side
        # it must go on.
        if value < node.value:
            # smaller than value: attach the result to the left
            node.Left = self._insert_recursive(node.left, value)
        elif value > node.value:
            # Larger: athhatch the result to the right
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
        """Bst search is often faster than a linear search because linear searches check items one at 
        time, through all the values, 0(n).a bst tree on the other had, each comparison directs to which side 
        the value must be on, skipping the other subtree.
        """
        pass

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        pass

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        pass

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
        pass


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



if __name__ == "__main__":
    main()