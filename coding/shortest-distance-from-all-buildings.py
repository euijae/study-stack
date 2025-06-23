"""
Problem Statement: Shortest Distance from All Buildings
You are given an m x n grid grid of values:

0 represents an empty land where you can build a house,

1 represents a building,

2 represents an obstacle that you cannot pass through or build on.

You want to build a house on an empty land such that the total travel distance to all buildings is minimized. The travel distance is calculated using Manhattan Distance, where distance(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

You can only move up, down, left, and right. You cannot pass through obstacles or buildings.

Return the shortest distance from an empty land to all buildings. If it is not possible, return -1.

🔒 Constraints:
m == grid.length

n == grid[i].length

1 <= m, n <= 50

grid[i][j] is 0, 1, or 2.

There will be at least one building in the grid.
"""
from typing import List
from collections import deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        total_buildings = 0
        dist_sum = [[0] * cols for _ in range(rows)]
        reach = [[0] * cols for _ in range(rows)]

        # iterate grid cell by cell
        for r in range(rows):
            for c in range(cols):
                # BFS from each building
                if grid[r][c] == 1:
                    total_buildings += 1
                    visited = set()
                    q = deque([(r, c, 0)]) # row, col, distance
                    visited.add((r, c))

                    while q:
                        x, y, dist = q.popleft()

                        for dx, dy in dirs:
                            nx, ny = x+dx, y+dy
                            # hasn't been visited and the cell at nx, ny must be an empty
                            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == 0: 
                                visited.add((nx, ny))
                                dist_sum[nx][ny] += dist+1
                                reach[nx][ny] += 1
                                q.append((nx, ny, dist+1))
        
        res = float('inf')
        res = min(
            (dist_sum[r][c] for r in range(rows) for c in range(cols) if reach[r][c] == total_buildings and grid[r][c] == 0),
            default = float('inf')
        )

        return res if res != float('inf') else -1



def run_tests():
    sol = Solution()

    test_cases = [
        (
            [[1, 0, 2, 0, 1],
             [0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0]],
            7  # expected output
        ),
        (
            [[1, 0],
             [0, 1]],
            2
        ),
        (
            [[1]],
            -1
        ),
        (
            [[1, 2, 0]],
            -1
        )
    ]

    for i, (grid, expected) in enumerate(test_cases, 1):
        result = sol.shortestDistance(grid)
        print(f"Test case {i}: {'✅' if result == expected else '❌'} (Expected: {expected}, Got: {result})")


if __name__ == "__main__":
    run_tests()