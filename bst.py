# class to represent a binary search tree
import queue


class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __contains__(self, data):
        if self._get(data, self.root):
            return True
        else:
            return False

    def __getitem__(self, data):
        return self.get(data)

    def __setitem__(self, data, value):
        self.put(data, value)

    def __delitem__(self, data):
        self.delete(data)

    def __repr__(self):
        return 'BST({})'.format(self.root)

    def __str__(self):
        return 'BST({})'.format(self.root)

    def put(self, data):
        if self.root:
            self._put(data, self.root)
        else:
            self.root = TreeNode(data)
        self.size += 1

    def _put(self, data, current_node):
        if data < current_node.data:
            if current_node.left:
                self._put(data, current_node.left)
            else:
                current_node.left = TreeNode(data)
        else:
            if current_node.right:
                self._put(data, current_node.right)
            else:
                current_node.right = TreeNode(data)

    def get(self, data):
        if self.root:
            res = self._get(data, self.root)
            if res:
                return res
            else:
                return None
        else:
            return None

    def _get(self, data, current_node):
        if data == current_node.data:
            return current_node
        elif data < current_node.data:
            if current_node.left:
                return self._get(data, current_node.left)
            else:
                return None
        else:
            if current_node.right:
                return self._get(data, current_node.right)
            else:
                return None

    def delete(self, data):
        if self.root:
            self.root = self._delete(data, self.root)

    def _delete(self, data, current_node):
        if data < current_node.data:
            if current_node.left:
                current_node.left = self._delete(data, current_node.left)
            else:
                return None
        elif data > current_node.data:
            if current_node.right:
                current_node.right = self._delete(data, current_node.right)
            else:
                return None
        else:
            if current_node.left and current_node.right:
                current_node.data = self.get_min(current_node.right).data
                current_node.right = self.remove_min(current_node.right)
            elif current_node.left:
                return current_node.left
            else:
                return current_node.right
        return current_node

    def remove(self, current_node):
        if current_node.left and current_node.right:
            successor = self.get_min(current_node.right)
            successor.right = self.remove_min(current_node.right)
            successor.left = current_node.left
            current_node.left = None
            current_node.right = None
            return successor
        elif current_node.left:
            return current_node.left
        else:
            return current_node.right

    def get_min(self, current_node):
        if current_node.left:
            return self.get_min(current_node.left)
        else:
            return current_node

    def remove_min(self, current_node):
        if current_node.left:
            current_node.left = self.remove_min(current_node.left)
        else:
            return current_node.right

    def get_max(self):
        return self._get_max(self.root)

    def _get_max(self, current_node):
        if current_node.right:
            return self._get_max(current_node.right)
        else:
            return current_node

    def remove_max(self):
        return self._remove_max(self.root)

    def _remove_max(self, current_node):
        if current_node.right:
            current_node.right = self._remove_max(current_node.right)
        else:
            return current_node.left
        return current_node

    def preorder(self):
        self._preorder(self.root)

    # tree traversals
    def _preorder(self, root):
        if root is None:
            return
        else:
            print(root.data)
            self._preorder(root.left)
            self._preorder(root.right)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, current_node):
        if current_node is None:
            return
        else:
            self._inorder(current_node.left)
            print(current_node.data)
            self._inorder(current_node.right)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, current_node):
        if current_node is None:
            return
        else:
            self._postorder(current_node.left)
            self._postorder(current_node.right)
            print(current_node.data)

    def levelorder(self):
        q = queue.Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            current_node = q.dequeue()
            print(current_node.data)
            if current_node.left:
                q.enqueue(current_node.left)
            if current_node.right:
                q.enqueue(current_node.right)

    def height(self):
        return self._height(self.root)

    def _height(self, current_node):
        if current_node is None:
            return 0
        else:
            left_height = self._height(current_node.left)
            right_height = self._height(current_node.right)
            return 1 + max(left_height, right_height)

    def is_balanced(self):
        return self._is_balanced(self.root)

    def _is_balanced(self, current_node):
        if current_node is None:
            return True
        else:
            left_height = self._height(current_node.left)
            right_height = self._height(current_node.right)
            return abs(left_height - right_height) <= 1 and self._is_balanced(
                current_node.left) and self._is_balanced(current_node.right)

    def search(self, data):
        return self._search(data, self.root)

    def _search(self, data, current_node):
        if current_node is None:
            return False
        elif current_node.data == data:
            return True
        elif data < current_node.data:
            return self._search(data, current_node.left)
        else:
            return self._search(data, current_node.right)
