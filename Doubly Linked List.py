class Node:
    """
    Node for Doubly Linked List.
    Attributes:
        data (any): Data held by the node.
        prev (Node): Reference to the previous node.
        next (Node): Reference to the next node.
    """
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """
    Doubly Linked List supporting insertion, deletion, and traversal.
    Each node points both to the previous and next node enabling bidirectional traversal.
    """

    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Append a node with `data` at the end of the list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        new_node.prev = last

    def prepend(self, data):
        """
        Insert a node with `data` at the beginning of the list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, node):
        """
        Delete a node from the list.
        Adjusts pointers of neighboring nodes accordingly.
        """
        if not self.head or not node:
            return

        # If node is head
        if self.head == node:
            self.head = node.next
            if self.head:
                self.head.prev = None
            return

        # If node is in the middle or end
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next

    def traverse_forward(self):
        """
        Traverse and print the list from head to tail.
        """
        current = self.head
        while current:
            print(current.data, end=" <-> " if current.next else "")
            current = current.next
        print()

    def traverse_backward(self):
        """
        Traverse and print the list from tail to head.
        """
        current = self.head
        if not current:
            return
        while current.next:
            current = current.next

        while current:
            print(current.data, end=" <-> " if current.prev else "")
            current = current.prev
        print()


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.prepend(5)
    dll.traverse_forward()   # 5 <-> 10 <-> 20
    dll.traverse_backward()  # 20 <-> 10 <-> 5

    # Delete middle node (10)
    node_to_delete = dll.head.next
    dll.delete(node_to_delete)
    dll.traverse_forward()   # 5 <-> 20
