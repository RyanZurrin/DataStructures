# class to represent a queue using a linked list

class Node(object):
    def __init__(self, data=None, next_=None, prev=None):
        self.data = data
        self.next = next_
        self.prev = prev


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def peek(self):
        return None if self.size == 0 else self.head.data

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def empty(self):
        self.head = None
        self.tail = None
        self.size = 0
