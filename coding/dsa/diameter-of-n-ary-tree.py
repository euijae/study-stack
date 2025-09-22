from typing import List
import unittest

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def diameter(self, root: 'Node') -> int:
        self.max_diameter = 0

        def dfs(node):
            if not node:
                return 0
            
            max1 = max2 = 0

            for child in node.children:
                height = dfs(child)
                if height > max1:
                    max2, max1 = max1, height
                elif height > max2:
                    max2 = height
                
                self.max_diameter = max(self.max_diameter, max1+max2)
            return 1+max1
        
        dfs(root)
        return self.max_diameter


class TestDiameterNaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.solution.diameter(None), 0)

    def test_single_node(self):
        root = Node(1)
        self.assertEqual(self.solution.diameter(root), 0)

    def test_linear_tree(self):
        # Tree: 1 -> 2 -> 3 -> 4
        node4 = Node(4)
        node3 = Node(3, [node4])
        node2 = Node(2, [node3])
        root = Node(1, [node2])
        self.assertEqual(self.solution.diameter(root), 3)

    def test_balanced_tree(self):
        #       1
        #    /  |  \
        #   2   3   4
        #       |
        #       5
        node5 = Node(5)
        node2 = Node(2)
        node3 = Node(3, [node5])
        node4 = Node(4)
        root = Node(1, [node2, node3, node4])
        self.assertEqual(self.solution.diameter(root), 3)

if __name__ == '__main__':
    unittest.main()
