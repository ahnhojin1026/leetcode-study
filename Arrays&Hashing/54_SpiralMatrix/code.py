class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        output = []
        # direction vectors: right, down, left, up
        delta = [[0,1],[1,0],[0,-1],[-1,0]]
        # initial position and direction
        x = 0
        y = 0
        direction = 0

        # traverse all elements
        for i in range(m*n):
            output.append(matrix[x][y])
            # mark as visited
            matrix[x][y] = -101
            # calculate next position
            nx = x + delta[direction][0]
            ny = y + delta[direction][1]
            
            # if next position is out of bounds or already visited, change direction
            if nx < 0 or nx >= m or ny < 0 or ny >=n or matrix[nx][ny] == -101:
                direction += 1
                direction = direction % 4
                nx = x + delta[direction][0]
                ny = y + delta[direction][1]
            # update position
            x = nx
            y = ny
            
        return output