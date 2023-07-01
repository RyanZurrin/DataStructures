# class for binary tree

class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BT:
    def __init__(self):
        self.root = None
        self.size = 0

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
        elif current_node.right:
            self._put(data, current_node.right)
        else:
            current_node.right = TreeNode(data)

    def get(self, data):
        if self.root:
            return res if (res := self._get(data, self.root)) else None
        else:
            return None

    def _get(self, data, current_node):
        if data == current_node.data:
            return current_node
        elif data < current_node.data:
            return self._get(data, current_node.left) if current_node.left else None
        else:
            return self._get(data, current_node.right) if current_node.right else None

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
        elif current_node.left and current_node.right:
            current_node.data = self.get_min(current_node.right)
            current_node.right = self._delete(current_node.data, current_node.right)
        elif current_node.left:
            return current_node.left
        elif current_node.right:
            return current_node.right
        else:
            return None
        return current_node

    # traversals
    def preorder(self, root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)

    def levelorder(self, root):
        if root:
            queue = [root]
            while queue:
                current_node = queue.pop(0)
                print(current_node.data)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)


