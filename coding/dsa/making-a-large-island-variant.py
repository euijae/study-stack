from typing import List

class Solution:
    def __init__(self):
        self.directions = [(-1,0),(0,1),(1,0),(0,-1)]
    
    def borders_land(self, grid, r, c):
        for dr, dc in self.directions:
            nr, nc = r+dr, c+dc
            if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == 0:
                continue
            return True
        return False

    def create_island(self, grid, visited, r, c):
        visited[r][c] = True
        size = 1
        for dr, dc in self.directions:
            nr, nc = r+dr, c+dc
            if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or visited[nr][nc] or self.borders_land(grid, nr, nc):
                continue
            size += self.create_island(grid, visited, nr, nc)
        return size
    
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        largest = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 or visited[r][c] or self.borders_land(grid, r, c):
                    continue
                largest = max(largest, self.create_island(grid, visited, r, c))
        return largest

grid = [
  [1,1,1,0,0],
  [1,0,1,0,0],
  [0,0,0,0,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]

sol = Solution()
print(sol.largestIsland(grid))