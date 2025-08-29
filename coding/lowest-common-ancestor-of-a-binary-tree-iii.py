class Node:
    def __init__(self, val: int, left: 'Node' = None, right: 'Node' = None, parent: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        return self.method2(p, q)
    
    def method1(self, p: 'Node', q: 'Node') -> 'Node':
        if not p or not q:
            return None
        
        runp, runq = p, q
        
        while runp != runq:
            runp = runp.parent if runp.parent else q
            runq = runq.parent if runq.parent else p
        
        return runp

    def method2(self, p: 'Node', q: 'Node') -> 'Node':
        if not p or not q:
            return None
        
        visited = set()
        while p:
            visited.add(p)
            p = p.parent
        while q:
            if q in visited:
                return q
            q = q.parent
        return None

# Helper to link parent pointers
def connect_parents(root: 'Node', parent: 'Node' = None):
    if root:
        root.parent = parent
        connect_parents(root.left, root)
        connect_parents(root.right, root)

# Helper to find node by value (for testing)
def find_node(root: 'Node', target: int) -> 'Node':
    if not root:
        return None
    if root.val == target:
        return root
    return find_node(root.left, target) or find_node(root.right, target)

# Test tree:
#        3
#       / \
#      5   1
#     / \ / \
#    6  2 0  8
#      / \
#     7   4

n3 = Node(3)
n5 = Node(5)
n1 = Node(1)
n6 = Node(6)
n2 = Node(2)
n0 = Node(0)
n8 = Node(8)
n7 = Node(7)
n4 = Node(4)

n3.left, n3.right = n5, n1
n5.left, n5.right = n6, n2
n1.left, n1.right = n0, n8
n2.left, n2.right = n7, n4

connect_parents(n3)  # set parent pointers

# Usage:
sol = Solution()
assert sol.lowestCommonAncestor(n5, n1).val == 3
assert sol.lowestCommonAncestor(n6, n4).val == 5
assert sol.lowestCommonAncestor(n7, n8).val == 3
print("All Passed!!")