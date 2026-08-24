class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numList = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        def isRowValid(board):
            checker = numList.copy()
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        continue
                    elif board[i][j] in checker:
                        checker.remove(board[i][j])
                    else:
                        return False
                checker = numList.copy()
            return True
        def isColValid(board):
            checker = numList.copy()
            for i in range(9):
                for j in range(9):
                    if board[j][i] == ".":
                        continue
                    elif board[j][i] in checker:
                        checker.remove(board[j][i])
                    else:
                        return False
                checker = numList.copy()
            return True
        def areSquaresValid(board):
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    checker = numList.copy()

                    for x in range(3):
                        for y in range(3):
                            cell = board[i + x][j + y]


                            if cell == ".":
                                continue
                            elif cell in checker:
                                checker.remove(cell)
                            else:
                                return False
            return True

        if isRowValid(board) and isColValid(board) and areSquaresValid(board):
            return True
        else:
            return False