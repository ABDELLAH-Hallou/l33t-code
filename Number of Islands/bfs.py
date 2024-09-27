from collections import deque
from typing import List
class Solution:


    def numIslands(self, grid: List[List[str]]) -> int:
        if not len(grid):
            return 0
        rows,cols = len(grid),len(grid[0])
        visited = set()
        island_num = 0
        
        def bfs(row,col):
            q = deque()
            visited.add((row,col))
            q.append((row,col))

            while q:
                row,col = q.popleft()
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                for rd,cd in directions:
                    r, c = rd+row,cd+col
                    if r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] =="1" and (row,col) not in visited:
                    bfs(row,col)
                    island_num +=1
        return island_num 
            
