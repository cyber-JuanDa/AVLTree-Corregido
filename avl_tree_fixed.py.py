import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class Avl:
    def getHeight(self, node):
        if node is None:
            return 0
        else:
            return node.height

    def getBalance(self, node):
        if node is None:
            return 0
        else:
            return self.getHeight(node.left) - self.getHeight(node.right)

    def updateHeight(self, node):
        if node:
            node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def _insert_recursive(self, root, value):
        if not root:
            return Node(value)

        if value < root.value:
            root.left = self._insert_recursive(root.left, value)
        elif value > root.value:
            root.right = self._insert_recursive(root.right, value)
        else:
            return root

        self.updateHeight(root)
        balance = self.getBalance(root)

        if balance > 1 and value < root.left.value:
            return self.rotate_right(root)
        if balance < -1 and value > root.right.value:
            return self.rotate_left(root)
        if balance > 1 and value > root.left.value:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and value < root.right.value:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root


class AVLTree:
    def __init__(self):
        self.root = None
        self.avl = Avl()

    def insert(self, value):
        self.root = self.avl._insert_recursive(self.root, value)


if __name__ == "__main__":
    avl = AVLTree()
    values_to_insert = [10, 20, 30, 40, 50, 25]

    print("Insertando valores:", values_to_insert)
    for val in values_to_insert:
        avl.insert(val)

    print("\n--- Después de inserciones ---")
