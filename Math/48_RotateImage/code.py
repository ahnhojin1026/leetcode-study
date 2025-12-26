class Solution:


    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        def turn_90(x: int, y: int) -> None:
            # swap_points = [[x,y],[y,n-1-x],[n-1-x,n-1-y],[n-1-y,x]]
            temp = matrix[x][y]
            # swap 4 points
            matrix[x][y] = matrix[n-1-y][x]
            matrix[n-1-y][x] = matrix[n-1-x][n-1-y]
            matrix[n-1-x][n-1-y] = matrix[y][n-1-x]
            matrix[y][n-1-x] = temp
            return
        
        # rotate the quater of the matrix
        # case if n is even number
        if n % 2 == 0:
            for x in range(n // 2):
                for y in range(n // 2):
                    turn_90(x,y)
        # case if n is odd number
        else:
            for x in range(n // 2 + 1):
                for y in range(n // 2):
                    turn_90(x,y)
        