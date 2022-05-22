class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)


class LinkedList:

    def __init__(self):
        # first node of LinkedList
        self.head = None
        self.num_of_nodes = 0

    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        # Very first insertion
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        # check if linked list is empty
        if self.head is None:
            self.head = new_node
        else:
            loop_node = self.head

            while loop_node.next_node is not None:
                loop_node = loop_node.next_node

            loop_node.next_node = new_node

    # O(1)
    def num_of_items(self):
        return self.num_of_nodes

    # O(n)
    def traverse(self):

        loop_node = self.head

        while loop_node is not None:
            print(loop_node)
            loop_node = loop_node.next_node

    # O(n) max running time
    def remove(self, data):

        # if linked list is empty
        if self.head is None:
            return

        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        # search miss
        if actual_node is None:
            return
        # Update references
        # if element to be delete is 1st element
        if previous_node is None:
            self.head = actual_node.next_node
        # if elements to be deleted is in btw
        else:
            previous_node.next_node = actual_node.next_node


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_start(10)
    linked_list.insert_start('Adam')
    linked_list.insert_end(20.8)
    linked_list.insert_end(80)
    linked_list.insert_end(90)
    linked_list.insert_end(100)
    linked_list.insert_end(2000)
    linked_list.traverse()
    print('------------------')
    linked_list.remove('Adam')
    linked_list.remove(90)
    linked_list.traverse()
