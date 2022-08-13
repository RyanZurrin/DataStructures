# class to represent a hash table


class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self):
        self.size = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0
        self.MAX_LOAD_FACTOR = 0.65
        self.prime_num = 5

    def __setitem__(self, key, value):
        hash_value = self._hash(key)
        item = HashItem(key, value)
        while self.slots[hash_value] is not None:
            if self.slots[hash_value].key is key:
                break
            hash_value = (hash_value + 1) % self.size

        if self.slots[hash_value] is None:
            self.count += 1
            self.slots[hash_value] = item
        self.check_growth()

    def __getitem__(self, key):
        hash_value = self._hash(key)
        while self.slots[hash_value] is not None:
            if self.slots[hash_value].key is key:
                return self.slots[hash_value].value
            hash_value = (hash_value + 1) % self.size
        return None

    def __contains__(self, key):
        hash_value = self._hash(key)
        if self.slots[hash_value] is None:
            return False
        else:
            if self.slots[hash_value].key == key:
                return True
            else:
                next_slot = self.slots[hash_value].next
                while next_slot is not None:
                    if next_slot.key == key:
                        return True
                    next_slot = next_slot.next
                return False

    def __len__(self):
        return self.count

    def __delitem__(self, key):
        hash_value = self._hash(key)
        if self.slots[hash_value] is None:
            raise KeyError
        else:
            if self.slots[hash_value].key == key:
                self.slots[hash_value] = self.slots[hash_value].next
                self.count -= 1
            else:
                next_slot = self.slots[hash_value].next
                while next_slot is not None:
                    if next_slot.key == key:
                        self.slots[hash_value].next = next_slot.next
                        self.count -= 1
                        break
                    next_slot = next_slot.next
                else:
                    raise KeyError

    def __iter__(self):
        for slot in self.slots:
            if slot is not None:
                yield slot.key

    def __repr__(self):
        return str(self.slots)

    def __str__(self):
        return str(self.slots)

    def _hash(self, key):
        mult = 1
        hash_val = 0
        for char in key:
            hash_val += ord(char) * mult
            mult += 1
        return hash_val % self.size

    def _hash2(self, key):
        mult = 1
        hash_val = 0
        for char in key:
            hash_val += ord(char) * mult
            mult += 1
        return hash_val

    def get_quadratic(self, key):
        hash_value = self._hash(key)
        j = 1
        while self.slots[hash_value] is not None:
            if self.slots[hash_value].key is key:
                return self.slots[hash_value].value
            hash_value = (hash_value + j * j) % self.size
            j += 1
        return None

    def put_quadratic(self, key, value):
        item = HashItem(key, value)
        hash_value = self._hash(key)
        j = 1
        while self.slots[hash_value] is not None:
            if self.slots[hash_value].key is key:
                break
            hash_value = (hash_value + j * j) % self.size
            j += 1
        if self.slots[hash_value] is None:
            self.count += 1
            self.slots[hash_value] = item
        self.check_growth()

    def put_doubleHashing(self, key, value):
        item = HashItem(key, value)
        hash_value = self._hash(key)
        j = 1
        while self.slots[hash_value] is not None:
            if self.slots[hash_value].key is key:
                break
            hash_value = (hash_value + j * (self.prime_num - (
                    self._hash2(key) % self.prime_num))) % self.size
            j += 1
        if self.slots[hash_value] is None:
            self.count += 1
            self.slots[hash_value] = item
        self.check_growth()

    def get_doubleHashing(self, key):
        hash_value = self._hash(key)
        j = 1
        while self.slots[hash_value] is not None:
            if self.slots[hash_value].key is key:
                return self.slots[hash_value].value
            hash_value = (hash_value + j * (self.prime_num - (
                    self._hash2(key) % self.prime_num))) % self.size
            j += 1
        return None

    def put(self, key, value):
        self.__setitem__(key, value)

    def get(self, key):
        return self.__getitem__(key)

    def check_growth(self):
        load_factor = self.count / self.size
        if load_factor > self.MAX_LOAD_FACTOR:
            print("load factor before resize: ", load_factor)
            self.resize()
            print("load factor after resize: ", self.count / self.size)

    def resize(self):
        new_hash_table = HashTable()
        new_hash_table.size = self.size * 2
        new_hash_table.slots = [None for i in range(new_hash_table.size)]

        for i in range(self.size):
            if self.slots[i] is not None:
                new_hash_table.put(self.slots[i].key, self.slots[i].value)

        self.slots = new_hash_table.slots
        self.size = new_hash_table.size

    def print_table(self):
        for i in range(self.size):
            if self.slots[i] is not None:
                print(self.slots[i].key, self.slots[i].value)
            else:
                print(None)


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
            self.tail = new_node
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
        self.slots = [None for i in range(self.size)]
        self.count = 0
        for x in range(self.size):
            self.slots[x] = SLL()

    def _hash(self, key):
        mult = 1
        hash_val = 0
        for char in key:
            hash_val += ord(char) * mult
            mult += 1
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
