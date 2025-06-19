class AVLNode:
    """
    Node class for AVL Tree
    Attributes:
        key (int): Value stored in the node.
        height (int): Height of the node in the tree.
        left (AVLNode): Left child node.
        right (AVLNode): Right child node.
    """
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    """
    AVL Tree implementation with insert and rotation methods to keep the tree balanced.
    Self-balancing BST ensuring O(log n) time complexity for search, insert, and delete.
    """

    def get_height(self, node):
        """Return height of node or 0 if None."""
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        """Calculate balance factor of node."""
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        """
        Right rotate subtree rooted with y.
        Returns new root after rotation.
        """
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    def left_rotate(self, x):
        """
        Left rotate subtree rooted with x.
        Returns new root after rotation.
        """
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def insert(self, root, key):
        """
        Recursive function to insert a key in subtree rooted with node and
        returns the new root of the subtree.
        """
        # Step 1 - Perform normal BST insertion
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Step 2 - Update the height of the ancestor node
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # Step 3 - Get the balance factor
        balance = self.get_balance(root)

        # Step 4 - If node is unbalanced, try the 4 cases of rotations

        # Case 1 - Left Left
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Case 2 - Right Right
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Case 3 - Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case 4 - Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        # Return the unchanged root pointer
        return root

    def pre_order(self, root):
        """Utility function to perform preorder traversal of the tree."""
        if not root:
            return
        print(f"{root.key} ", end="")
        self.pre_order(root.left)
        self.pre_order(root.right)


# Example usage
if __name__ == "__main__":
    avl = AVLTree()
    root = None

    values = [10, 20, 30, 40, 50, 25]
    for val in values:
        root = avl.insert(root, val)

    print("Preorder traversal of AVL tree is:")
    avl.pre_order(root)
