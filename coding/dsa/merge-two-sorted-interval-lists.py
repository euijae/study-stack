from typing import List

class Solution:
         
    def mergeTwoSortedIntervals(self, list1: List[List[int]], list2: List[List[int]]) -> List[List[int]]:
        i = j = 0
        merged = []
        def insertInterval(interval: List[int]):
            if merged and merged[-1][1] >= interval[0]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)

        while i < len(list1) or j < len(list2):
            if j >= len(list2) or (i < len(list1) and list1[i][0] < list2[j][0]): # earlier start comes first
                insertInterval(list1[i])
                i += 1
            else:
                insertInterval(list2[j])
                j += 1
        print(merged)
        return merged
        

list1 = [[1,3],[5,7],[9,12]] 
list2 = [[2,4],[6,8]]

sol = Solution()
print(sol.mergeTwoSortedIntervals(list1, list2) == [[1,4],[5,8],[9,12]])
# Output: [[1,4],[5,8],[9,12]]