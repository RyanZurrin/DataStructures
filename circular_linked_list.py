# class to represent a circular linked list

class Node:
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.next = nxt
        self.prev = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        if self.size == 0:
            return 'Empty'
        current = self.head
        string = ''
        while current:
            string += f'{str(current.data)} '
            current = current.next
            if current == self.head:
                break
        return string

    def __len__(self):
        return self.size

    def __iter__(self):
        return self

    def __next__(self):
        if self.head is None:
            raise StopIteration
        current = self.head
        self.head = self.head.next
        return current.data

    def __contains__(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def __getitem__(self, index):
        if index >= self.size:
            raise IndexError('Index out of range')
        current = self.head
        for _ in range(index):
            current = current.next
            if current == self.head:
                break
        return current.data

    def __setitem__(self, index, data):
        if index >= self.size:
            raise IndexError('Index out of range')
        current = self.head
        for _ in range(index):
            current = current.next
            if current == self.head:
                break
        current.data = data

    def __delitem__(self, index):
        if index >= self.size:
            raise IndexError('Index out of range')
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index):
                current = current.next
                if current == self.head:
                    break
            current.prev.next = current.next
            current.next.prev = current.prev
        self.size -= 1
        if self.size == 0:
            self.head = None
            self.tail = None
        elif index == self.size:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            new_node.prev = self.tail
            self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail
        self.size += 1

    def append_at_location(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
                if current == self.head:
                    break
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
            if current == self.head:
                break
        return False

    def remove(self, data):
        cur = self.head
        prev = self.head
        while prev == cur or prev != self.tail:
            if cur.data == data:
                if cur == self.head:
                    self.head = cur.next
                    self.tail.next = self.head
                elif cur == self.tail:
                    self.tail = prev
                    prev.next = self.head
                else:
                    prev.next = cur.next
                self.size -= 1
                return
            prev = cur
            cur = cur.next

    def remove_duplicates(self):
        """ Removes all duplicates from the list list leaving only unique
        elements. Uses a hash table to keep track of the elements in the list.
        """
        hash_table = {}
        current = self.head
        while current:
            if current.data in hash_table:
                print('Removing duplicate:', current.data)
                self.remove(current.data)
            else:
                hash_table[current.data] = True
            current = current.next
            if current == self.head:
                break

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
