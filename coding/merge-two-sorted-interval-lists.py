from typing import List

class Solution:
    def mergeTwoSortedIntervals(self, list1: List[List[int]], list2: List[List[int]]) -> List[List[int]]:
        # Step 1: Merge the two sorted lists by start time
        merged = []
        i = j = 0
        
        while i < len(list1) and j < len(list2):
            if list1[i][0] < list2[j][0]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        
        # Append remaining intervals
        while i < len(list1):
            merged.append(list1[i])
            i += 1
        while j < len(list2):
            merged.append(list2[j])
            j += 1
        
        # Step 2: Merge overlapping intervals in merged list
        result = []
        for interval in merged:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        
        return result

list1 = [[1,3],[5,7],[9,12]]
list2 = [[2,4],[6,8]]

sol = Solution()
print(sol.mergeTwoSortedIntervals(list1, list2) == [[1,4],[5,8],[9,12]])
# Output: [[1,4],[5,8],[9,12]]