from bst_operations.node import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def insertNode(self, value):
        self.root, inserted_position = BinarySearchTree.insert(self.root, value, 1)
        return inserted_position
    
    def deleteNode(self, value):
        self.root, deleted_position = BinarySearchTree.delete(self.root, value, 1)
        return deleted_position

    @staticmethod
    def min(node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    @staticmethod
    def insert(node, value, pos):
        if node is None:
            return Node(value), pos 

        if node.value > value:
            node.left, inserted_position = BinarySearchTree.insert(node.left, value, pos * 2)
        elif node.value < value:
            node.right, inserted_position = BinarySearchTree.insert(node.right, value, pos * 2 + 1)
        else:
            inserted_position = -1
        return node, inserted_position

    @staticmethod
    def delete(node, value, pos):
        if node is None:
            return node, -1
        else:
            if value > node.value:
                node.right, deleted_position = BinarySearchTree.delete(node.right, value, pos * 2 + 1)
            elif value < node.value:
                node.left, deleted_position = BinarySearchTree.delete(node.left, value, pos * 2)
            else:
                deleted_position = pos
                if node.left is None:
                    node = node.right
                elif node.right is None:
                    node = node.left
                else:
                    node.value = BinarySearchTree.min(node.right).value
                    node.right, _ = BinarySearchTree.delete(node.right, node.value, pos * 2 + 1)
            return node, deleted_position