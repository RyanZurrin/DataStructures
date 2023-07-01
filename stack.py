# class representing a stack using a linked list

class Node:
    def __init__(self, data=None, next_=None):
        self.next = next_
        self.data = data


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self

    def __next__(self):
        if self.top:
            data = self.top.data
            self.top = self.top.next
            return data
        else:
            raise StopIteration

    def __str__(self):
        if self.top:
            node = self.top
            while node.next:
                print(node.data, end=' -> ')
                node = node.next
            print(node.data)
        else:
            print('Stack is empty')

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if not self.top:
            raise Exception('Stack is empty')
        data = self.top.data
        self.size -= 1
        self.top = self.top.next if self.top.next else None
        return data

    def peek(self):
        if self.top:
            return self.top.data
        else:
            raise Exception('Stack is empty')

    def is_empty(self):
        return self.size == 0


def check_brackets(expression):
    brackets_stack = Stack()
    last = ' '
    for char in expression:
        if char in ('(', '[', '{'):
            brackets_stack.push(char)
        if char in (']', '}', ')'):
            last = brackets_stack.pop()
            if (
                last == '['
                and char == ']'
                or last == '{'
                and char == '}'
                or last == '('
                and char == ')'
            ):
                continue
            else:
                return False
        return brackets_stack.size <= 0
