# class to represent a priority queue

class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data, priority):
        node = Node(data, priority)
        self.queue.append(node)
        self.queue.sort()

    def dequeue(self):
        return self.queue.pop(0).data

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        return self.queue[0].data

    def size(self):
        return len(self.queue)

    def print_queue(self):
        for node in self.queue:
            print(f"{str(node.data)} - {str(node.priority)}")
