# class to represent a singly linked list

class Node:
    def __init__(self, data=None, next_=None):
        self.data = data
        self.next = next_


class SinglyLinkedList:
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
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        self.size += 1

    def append_at_location(self, data, index):
        if index == 0:
            self.head = Node(data, self.head)
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = Node(data, current.next)
            if current.next.next is None:
                self.tail = current.next
        self.size += 1

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

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


