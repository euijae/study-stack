from typing import List
import heapq

"""
    Original: https://leetcode.com/problems/merge-k-sorted-lists/
    Variants:
        1) Merge K sorted array list
        2) Merge K sorted Iterators
"""
class Solution:
    def mergeKLists(self, lists: List[List[int]]) -> List[int]:
        heap = [] # triple (arr index, val index, val)
        for i, arr in enumerate(lists):
            if arr:
                heapq.heappush(heap, (arr[0], i, 0))
        print(heap)
        res = []
        while heap:
            val, arr_index, val_index = heapq.heappop(heap)
            res.append(val)

            if val_index < len(lists[arr_index])-1:
                heapq.heappush(heap, (lists[arr_index][val_index+1], arr_index, val_index+1))

        return res
    

solution = Solution()
print(solution.mergeKLists([[1,3], [2], [4,5]]))