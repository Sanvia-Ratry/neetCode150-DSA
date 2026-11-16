class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cubeHash = defaultdict(set)
        
        for i in range(9):
            colSet = set()
            rowSet = set()

            for j in range(9):
                r = (i//3)
                c = (j//3)
                if board[i][j] != ".":
                    if board[i][j] in cubeHash[(r,c)]:
                        return False
                    if board[i][j] not in cubeHash[(r,c)]:
                        cubeHash[(r,c)].add(board[i][j])

                    if board[i][j] not in rowSet:
                        rowSet.add(board[i][j])
                    else:
                        return False
                
                if board[j][i] != ".":
                    if board[j][i] not in colSet:
                        colSet.add(board[j][i])
                    else:
                        return False
                
                
        return True