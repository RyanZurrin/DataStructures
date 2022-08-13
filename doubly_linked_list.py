# class to represent a doubly linked list

class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        if self.size == 0:
            return 'Empty'
        else:
            current = self.head
            string = ''
            while current:
                string += str(current.data) + ' '
                current = current.next
            return string

    def __len__(self):
        return self.size

    def __iter__(self):
        return self

    def __next__(self):
        if self.head is None:
            raise StopIteration
        else:
            current = self.head
            self.head = self.head.next
            return current.data

    def __contains__(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def __getitem__(self, index):
        if index >= self.size:
            raise IndexError('Index out of range')
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, data):
        if index >= self.size:
            raise IndexError('Index out of range')
        current = self.head
        for i in range(index):
            current = current.next
        current.data = data

    def __delitem__(self, index):
        if index >= self.size:
            raise IndexError('Index out of range')
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
            if current.next is None:
                self.tail = current
        self.size -= 1

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def append_at_location(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
            new_node.prev = current
        self.size += 1

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def insert(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
            new_node.prev = current
        self.size += 1

    def remove(self, data):
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next
        raise ValueError('Data not found')

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
