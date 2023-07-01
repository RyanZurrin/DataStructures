import bst
import stack

expr = "4 5 + 5 3 - *".split()

stack = stack.Stack()

for term in expr:
    if term in "+-*/":
        node = bst.TreeNode(term)
        node.right = stack.pop()
        node.left = stack.pop()
    else:
        node = bst.TreeNode(int(term))
    stack.push(node)


def calc(node):
    left = calc(node.left) if node.left else 0
    right = calc(node.right) if node.right else 0
    if node.data == "*":
        return left * right
    elif node.data == "+":
        return left + right
    elif node.data == "-":
        return left - right
    elif node.data == "/":
        return left / right
    else:
        return node.data


root = stack.pop()
result = calc(root)
print(result)
