from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        # BFS
        def bfs(starts):
            # queue for BFS
            queue = deque(starts)
            # set to record visited cells
            visited = set(starts)
            
            while queue:
                r, c = queue.popleft()
                
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        if heights[nr][nc] >= heights[r][c]:
                            visited.add((nr, nc))
                            queue.append((nr, nc))
            return visited

        pacific_starts = []
        atlantic_starts = []
        
        # initialized with edge cells
        for i in range(m):
            pacific_starts.append((i, 0))
            atlantic_starts.append((i, n-1))
            
        for i in range(n):
            pacific_starts.append((0, i))
            atlantic_starts.append((m-1, i))

        p_visited = bfs(pacific_starts)
        a_visited = bfs(atlantic_starts)
        # return intersection
        return list(p_visited & a_visited)