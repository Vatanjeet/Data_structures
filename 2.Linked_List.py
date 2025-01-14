class Node:
    def __init__(self, data):
        self.data = data  # Value stored in the node
        self.next_node = None  # Pointer to the next node


class LinkedList:
    def __init__(self):
        self.head_node = None  # Start of the linked list
        self.node_count = 0  # Number of nodes in the linked list

    def __len__(self):
        return self.node_count

    def insert_at_head(self, value):
        """
        Insert a new node with the given value at the beginning of the linked list.
        """
        new_node = Node(value)  # Create a new node
        new_node.next_node = self.head_node  # Link the new node to the current head
        self.head_node = new_node  # Update head to the new node
        self.node_count += 1  # Increment the node count

    def insert_after(self, target_value, value):
        """
        Insert a new node with the given value after the first node that contains target_value.
        """
        new_node = Node(value)
        current_node = self.head_node

        # Traverse the list to find the target value
        while current_node is not None:
            if current_node.data == target_value:
                break
            current_node = current_node.next_node

        # If the target value is found, insert the new node
        if current_node is not None:
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node
            self.node_count += 1
        else:
            return 'Target value not found in the list.'

    def append_to_tail(self, value):
        """
        Append a new node with the given value at the end of the linked list.
        """
        new_node = Node(value)

        if self.head_node is None:  # If the list is empty
            self.head_node = new_node
            self.node_count += 1
            return

        current_node = self.head_node

        # Traverse to the last node
        while current_node.next_node is not None:
            current_node = current_node.next_node

        # Add the new node at the end
        current_node.next_node = new_node
        self.node_count += 1

    def pop(self):
        """
        Remove and return the last node in the linked list.
        """
        if self.head_node is None:  # If the list is empty
            return 'The linked list is empty.'

        current_node = self.head_node

        # If there's only one node, remove it
        if current_node.next_node is None:
            return self.delete_head()

        # Traverse to the second-to-last node
        while current_node.next_node.next_node is not None:
            current_node = current_node.next_node

        # Remove the last node
        current_node.next_node = None
        self.node_count -= 1

    def delete_head(self):
        """
        Remove the head node from the linked list.
        """
        if self.head_node is None:  # If the list is empty
            return 'The linked list is empty.'

        self.head_node = self.head_node.next_node  # Move head to the next node
        self.node_count -= 1

    def search(self, value):
        """
        Search for the first occurrence of a node containing the given value.
        Returns the position (0-indexed) or 'Not Found' if the value is not in the list.
        """
        current_node = self.head_node
        position = 0

        while current_node is not None:
            if current_node.data == value:
                return position
            current_node = current_node.next_node
            position += 1

        return 'Not Found'

    def clear(self):
        """
        Clear the entire linked list.
        """
        self.head_node = None
        self.node_count = 0

    def __str__(self):
        """
        String representation of the linked list.
        """
        result = ''
        current_node = self.head_node

        while current_node is not None:
            result += str(current_node.data) + ' -> '
            current_node = current_node.next_node

        return result[:-4]  # Remove the last arrow


ll = LinkedList()
ll.insert_at_head(10)
ll.insert_at_head(20)
ll.append_to_tail(30)
print(ll)  # Output: 20 -> 10 -> 30

ll.insert_after(10, 25)
print(ll)  # Output: 20 -> 10 -> 25 -> 30

ll.pop()
print(ll)  # Output: 20 -> 10 -> 25
