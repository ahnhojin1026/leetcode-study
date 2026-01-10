from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # BFS to mark the island
        def bfs_island(x: int, y: int):
            queue = deque([(x,y)])
            # mark as visited
            grid[x][y] = "#"
            # BFS traversal
            while queue:
                cur = queue.popleft()
                for (dx,dy) in delta:
                    nx = cur[0] + dx
                    ny = cur[1] + dy
                    # check boundary
                    if nx>=0 and nx<m and ny>=0 and ny<n:
                        # check if it's land
                        if grid[nx][ny] == "1":
                            queue.append((nx,ny))
                            grid[nx][ny] = "#"

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs_island(i,j)
                    ans += 1

        return ans