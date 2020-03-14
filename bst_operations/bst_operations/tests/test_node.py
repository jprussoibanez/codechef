import unittest

from bst_operations.node import Node

class TestNode(unittest.TestCase):
    def test_node_value(self):
        """
        Test that it can sum a list of integers
        """
        node = Node(1)
        result = node.value
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()