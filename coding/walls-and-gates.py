from typing import List
from collections import deque

"""
Problem Statement: Walls and Gates
You are given an m x n grid rooms initialized with these three possible values:

- -1 represents a wall or an obstacle.
- 0 represents a gate.

INF represents an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, leave it as INF.

Input: rooms = [
  [2147483647, -1, 0, 2147483647],
  [2147483647, 2147483647, 2147483647, -1],
  [2147483647, -1, 2147483647, -1],
  [0, -1, 2147483647, 2147483647]
]
Output: [
  [3, -1, 0, 1],
  [2, 2, 1, -1],
  [1, -1, 2, -1],
  [0, -1, 3, 4]
]
"""

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        self.dfs(rooms)

    def dfs(self, rooms: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(rooms), len(rooms[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r, c, dist):
            if r<0 or r >= rows or c < 0 or c >= cols or rooms[r][c] < dist:
                return
            
            rooms[r][c] = dist
            list(map(lambda d: dfs(r+d[0], c+d[1], dist+1), directions))
        
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    dfs(r, c, 0)


    def bfs(self, rooms: List[List[int]]) -> None:
        """
        Modify rooms in-place.
        """
        INF = 2147483647
        rows, cols = len(rooms), len(rooms[0])
        q = deque((r, c, 0) for r in range(rows) for c in range(cols) if rooms[r][c] == 0)
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            r, c, dist = q.popleft()

            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if 0<=nr<rows and 0<=nc<cols and rooms[nr][nc] == INF:
                    rooms[nr][nc] = dist+1
                    q.append((nr, nc, dist+1))


# Test input
INF = 2147483647
rooms = [
    [INF, -1, 0, INF],
    [INF, INF, INF, -1],
    [INF, -1, INF, -1],
    [0, -1, INF, INF]
]

# Instantiate and call
sol = Solution()
sol.wallsAndGates(rooms)

# Print the result
for row in rooms:
    print(row)