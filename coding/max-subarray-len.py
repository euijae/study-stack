from typing import List

# TODO - incomplete
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_map = {}  # prefix_sum -> earliest index seen
        max_len = 0

        for i, num in enumerate(nums):
            prefix_sum += num

            if prefix_sum == k:
                max_len = max(max_len, i+1)
            
            if prefix_sum - k in prefix_map:
                max_len = max(max_len, i - prefix_map[prefix_sum-k])
            
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i
        
        return max_len

import unittest

class TestMaxSubArrayLen(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1, -1, 5, -2, 3]
        k = 3
        self.assertEqual(self.solution.maxSubArrayLen(nums, k), 4)

    def test_example2(self):
        nums = [-2, -1, 2, 1]
        k = 1
        self.assertEqual(self.solution.maxSubArrayLen(nums, k), 2)

    def test_entire_array(self):
        nums = [1, 2, 3]
        k = 6
        self.assertEqual(self.solution.maxSubArrayLen(nums, k), 3)

    def test_no_subarray(self):
        nums = [1, 2, 3]
        k = 7
        self.assertEqual(self.solution.maxSubArrayLen(nums, k), 0)

    def test_multiple_valid_subarrays(self):
        nums = [1, 2, -1, 2, -1, 2]
        k = 3
        self.assertEqual(self.solution.maxSubArrayLen(nums, k), 5)

    def test_negative_k(self):
        nums = [1, -1, -1, 1, 1]
        k = -1
        self.assertEqual(self.solution.maxSubArrayLen(nums, k), 2)

if __name__ == '__main__':
    unittest.main()
            