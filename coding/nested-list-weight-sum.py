from typing import List
from collections import deque
import unittest

class NestedInteger:
    def isInteger(self) -> bool:
        """
        Return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        Return the single integer that this NestedInteger holds,
        if it holds a single integer.
        Return None if this NestedInteger holds a nested list.
        """

    def getList(self) -> ['NestedInteger']:
        """
        Return the nested list that this NestedInteger holds,
        if it holds a nested list.
        Return None if this NestedInteger holds a single integer.
        """

class Solution:
    def depthSum(self, nestedList: List['NestedInteger']) -> int:
        if not nestedList:
            return 0
        
        q = deque(nestedList)
        res = 0
        depth = 1

        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr.isInteger():
                    res += curr.getInteger()*depth
                else:
                    q.extend(curr.getList())
            
            depth += 1
        
        return res

class MockNestedInteger:
    def __init__(self, value):
        if isinstance(value, int):
            self._integer = value
            self._list = None
        else:
            self._integer = None
            self._list = value

    def isInteger(self):
        return self._integer is not None

    def getInteger(self):
        return self._integer

    def getList(self):
        return self._list

class TestNestedListWeightSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_integer(self):
        nestedList = [MockNestedInteger(5)]
        self.assertEqual(self.solution.depthSum(nestedList), 5)

    def test_nested_list(self):
        # Represents [1,[4,[6]]]
        nestedList = [
            MockNestedInteger(1),
            MockNestedInteger([
                MockNestedInteger(4),
                MockNestedInteger([
                    MockNestedInteger(6)
                ])
            ])
        ]
        # Expected sum = 1*1 + 4*2 + 6*3 = 27
        self.assertEqual(self.solution.depthSum(nestedList), 27)

    def test_empty_list(self):
        nestedList = []
        self.assertEqual(self.solution.depthSum(nestedList), 0)

if __name__ == '__main__':
    unittest.main()
