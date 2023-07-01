# class to represent a min heap

class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def __iter__(self):
        return self.heap.__iter__()

    def __str__(self):
        return str(self.heap[1:])

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        return self.heap[key]

    def __setitem__(self, key, value):
        self.heap[key] = value
        self.arrange(key)
        if key > self.size:
            self.size = key

    def arrange(self, k):
        while k // 2 > 0:
            if self.heap[k] < self.heap[k // 2]:
                self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
            k //= 2

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.arrange(self.size)

    def min_child(self, k):
        if k * 2 + 1 > self.size:
            return k * 2
        else:
            return k * 2 if self.heap[k * 2] < self.heap[k * 2 + 1] else k * 2 + 1

    def sink(self, k):
        while k * 2 <= self.size:
            mc = self.min_child(k)
            if self.heap[k] > self.heap[mc]:
                self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]
            k = mc

    def delete_root(self):
        if self.size == 0:
            return
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self.sink(1)
        return item

    def delete_at_location(self, loc):
        if loc > self.size:
            return
        item = self.heap[loc]
        self.heap[loc] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self.sink(loc)
        return item

    def heap_sort(self):
        sorted_list = []
        for _ in range(self.size):
            n = self.delete_root()
            sorted_list.append(n)

        return sorted_list

