import unittest

from bst_operations.binarysearchtree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    def test_empty_binarysearchtree(self):
        bst = BinarySearchTree()
        self.assertIsNone(bst.root)
    
    def test_insert_one_node(self):
        #Arrange
        bst = BinarySearchTree()
        
        #Act
        inserted_position = bst.insertNode(1)
        
        #Assert
        self.assertEqual(bst.root.value, 1)
        self.assertEqual(inserted_position, 1)
    
    def test_insert_one_left_node(self):
        #Arrange
        bst = BinarySearchTree()
        bst.insertNode(2)
        
        #Act
        inserted_position = bst.insertNode(1)

        #Assert
        self.assertEqual(bst.root.left.value, 1)
        self.assertEqual(inserted_position, 2)
    
    def test_insert_one_right_node(self):
        #Arrange
        bst = BinarySearchTree()
        bst.insertNode(2)
        
        #Act
        inserted_position = bst.insertNode(3)
        
        #Assert
        self.assertEqual(bst.root.right.value, 3)
        self.assertEqual(inserted_position, 3)
    
    def test_delete_one_node(self):
        #Arrange
        bst = BinarySearchTree()
        bst.insertNode(1)
        
        #Act
        deleted_position = bst.deleteNode(1)
        
        #Assert
        self.assertIsNone(bst.root)
        self.assertEqual(deleted_position, 1)
    
    def test_delete_one_left_node(self):
        #Arrange
        bst = BinarySearchTree()
        bst.insertNode(2)
        bst.insertNode(1)

        #Act
        deleted_position = bst.deleteNode(1)
        
        #Assert
        self.assertIsNone(bst.root.left)
        self.assertEqual(deleted_position, 2)
    
    def test_delete_one_right_node(self):
        #Arrange
        bst = BinarySearchTree()
        bst.insertNode(2)
        bst.insertNode(3)
        
        #Act
        deleted_position = bst.deleteNode(3)
        
        #Assert
        self.assertIsNone(bst.root.right)
        self.assertEqual(deleted_position, 3)

    def test_delete_root(self):
        #Arrange
        bst = BinarySearchTree()
        bst.insertNode(2)
        bst.insertNode(3)
        
        #Act
        deleted_position = bst.deleteNode(2)
        
        #Assert
        self.assertEqual(bst.root.value, 3)
        self.assertEqual(deleted_position, 1)
    
    def test_delete_non_existant_value(self):
        #Arrange
        bst = BinarySearchTree()
        bst.insertNode(1)
        
        #Act
        deleted_position = bst.deleteNode(2)
        
        #Assert
        self.assertEqual(bst.root.value, 1)
        self.assertEqual(deleted_position, -1)
    
    def test_insert_same_value(self):
        #Arrange
        bst = BinarySearchTree()
        bst.insertNode(1)
        
        #Act
        inserted_position = bst.insertNode(1)
        
        #Assert
        self.assertEqual(bst.root.value, 1)
        self.assertEqual(inserted_position, -1)
    
    def test_delete_twice_root_right(self):
        #Arrange
        bst = BinarySearchTree()
        bst.insertNode(1)
        bst.insertNode(3)
        bst.deleteNode(1)
        
        #Act
        deleted_position = bst.deleteNode(3)
        
        #Assert
        self.assertIsNone(bst.root)
        self.assertEqual(deleted_position, 1)
    
    def test_delete_twice_leaf_right(self):
        #Arrange
        bst = BinarySearchTree()
        bst.insertNode(1)
        bst.insertNode(3)
        bst.deleteNode(3)
        
        #Act
        deleted_position = bst.deleteNode(1)
        
        #Assert
        self.assertIsNone(bst.root)
        self.assertEqual(deleted_position, 1)
    
    def test_delete_twice_root_left(self):
        #Arrange
        bst = BinarySearchTree()
        bst.insertNode(3)
        bst.insertNode(1)
        bst.deleteNode(3)
        
        #Act
        deleted_position = bst.deleteNode(1)
        
        #Assert
        self.assertIsNone(bst.root)
        self.assertEqual(deleted_position, 1)
    
    def test_delete_twice_leaf_left(self):
        #Arrange
        bst = BinarySearchTree()
        bst.insertNode(3)
        bst.insertNode(1)
        bst.deleteNode(1)
        
        #Act
        deleted_position = bst.deleteNode(3)
        
        #Assert
        self.assertIsNone(bst.root)
        self.assertEqual(deleted_position, 1)

if __name__ == '__main__':
    unittest.main()