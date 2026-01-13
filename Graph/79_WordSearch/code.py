class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        # Traverse the board using DFS and backtracking
        def dfs(x: int, y: int, cur_index: int) -> bool:
            # traversed all characters in the word and match => return True
            if cur_index >= len(word):
                return True
            # out of bound => return False
            if x < 0 or x>=m or y < 0 or y>=n:
                return False
            # already visited => return False
            if board[x][y] == "#":
                return False
            # check character match
            if word[cur_index] == board[x][y]:
                # mark as visited (inplace modification)
                tmp = board[x][y]
                board[x][y] = "#"
                # explore all 4 directions
                if dfs(x+1,y,cur_index+1) or dfs(x-1,y,cur_index+1) or dfs(x,y+1,cur_index+1) or dfs(x,y-1,cur_index+1):
                    return True
                # backtrack
                board[x][y] = tmp
                return False
            else:
                return False
            
        # start DFS only from the cells that match the first character of the word
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
                    
        return False