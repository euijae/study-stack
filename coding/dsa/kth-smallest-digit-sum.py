import heapq

class Solution:
    def compute(self, num):
        res = 0
        while num:
            res += num % 10
            num //= 10
            
        return res

    def kth_smallest_digit_sum(self, nums, k):
        heap = []
        for i, num in enumerate(nums):
            dsum = self.compute(num)
            heapq.heappush(heap, (-dsum, -i, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for _, _, num in heap][::-1]

solution = Solution()
print(solution.kth_smallest_digit_sum([111, 84, 21, 12, 3, 56, 2001, 10000], 3))