# class to represent a hash table with chaining for collision resolution

class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, key, value):
        new_node = HashNode(key, value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.key, "--", current.value)
            current = current.next

    def search(self, key):
        current = self.head
        while current is not None:
            if current.key is key:
                print("Record found: ", current.key, "--", current.value)
                return True
            current = current.next
        return False


class HashTableChaining:
    def __init__(self):
        self.size = 6
        self.slots = [None for _ in range(self.size)]
        self.count = 0
        for x in range(self.size):
            self.slots[x] = SLL()

    def _hash(self, key):
        hash_val = sum(ord(char) * mult for mult, char in enumerate(key, start=1))
        return hash_val % self.size

    def put(self, key, value):
        hash_value = self._hash(key)
        node = HashNode(key, value)
        self.slots[hash_value].append(key, value)
        self.count += 1

    def get(self, key):
        hash_value = self._hash(key)
        return self.slots[hash_value].search(key)

    def print_table(self):
        print("Hash table is :- \n")
        print("Index \t Key \t Value")
        for i in range(self.size):
            print(i, end="\t\n")
            self.slots[i].traverse()