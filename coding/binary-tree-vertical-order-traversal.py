"""
🔢 Problem: Binary Tree Vertical Order Traversal
Given the root of a binary tree, return the vertical order traversal of its nodes' values.
(i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

🧠 Constraints:
The number of nodes in the tree is in the range [0, 1000].

-2³¹ <= Node.val <= 2³¹ - 1
"""


from typing import Optional, List
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional['TreeNode']) -> List[List[int]]:
        """
        Given the root of a binary tree, return the vertical order traversal 
        of its nodes' values. (i.e., from top to bottom, column by column).

        If two nodes are in the same row and column, the order should be from left to right.

        :param root: Root node of the binary tree
        :return: List of vertical order traversal, one list per column
        """
        if not root:
            return []
        
        col_group, q = defaultdict(list), deque([(root, 0)])

        while q:
            curr_node, col = q.popleft()
            col_group[col].append(curr_node.val)

            if curr_node.left:
                q.append((curr_node.left, col-1))
            if curr_node.right:
                q.append((curr_node.right, col+1))
        
        return [col_group[col] for col in sorted(col_group)]
        

# Helper to build a tree from level order list
def build_tree(level: List[Optional[int]]) -> Optional[TreeNode]:
    if not level:
        return None
    root = TreeNode(level[0])
    queue = deque([root])
    i = 1
    while queue and i < len(level):
        node = queue.popleft()
        if level[i] is not None:
            node.left = TreeNode(level[i])
            queue.append(node.left)
        i += 1
        if i < len(level) and level[i] is not None:
            node.right = TreeNode(level[i])
            queue.append(node.right)
        i += 1
    return root

# Instantiate solution
sol = Solution()

# Test cases
test_cases = [
    ([3,9,20,None,None,15,7], [[9],[3,15],[20],[7]]),
    ([1,2,3,4,5,6,7], [[4],[2],[1,5,6],[3],[7]]),
    ([], []),
    ([1,2,3,4,None,None,5], [[4],[2],[1],[3],[5]]),
    ([0,8,1,None,None,3,2,4,5,None,7,6],[[4], [8,3], [0,5,7], [1], [2], [6]])
]

# Run tests
for idx, (tree_data, expected) in enumerate(test_cases, 1):
    tree = build_tree(tree_data)
    output = sol.verticalOrder(tree)
    print(f"Test Case {idx}:")
    print(f"Input Tree: {tree_data}")
    print(f"Expected  : {expected}")
    print(f"Output    : {output}")
    print('-' * 40)
