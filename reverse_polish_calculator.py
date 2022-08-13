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
    if node.left:
        left = calc(node.left)
    else:
        left = 0
    if node.right:
        right = calc(node.right)
    else:
        right = 0
    if node.data == "+":
        return left + right
    elif node.data == "-":
        return left - right
    elif node.data == "*":
        return left * right
    elif node.data == "/":
        return left / right
    else:
        return node.data


root = stack.pop()
result = calc(root)
print(result)
