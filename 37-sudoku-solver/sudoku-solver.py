class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]  
        cols = [set() for _ in range(9)]  
        boxes = [set() for _ in range(9)]  

        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + (j // 3)].add(num)

        def backtrack(row, col):
            if row == 9: 
                return True
            if col == 9:  
                return backtrack(row + 1, 0)
            if board[row][col] != ".":  
                return backtrack(row, col + 1)

            box_index = (row // 3) * 3 + (col // 3)  
            for num in "123456789":
                if num not in rows[row] and num not in cols[col] and num not in boxes[box_index]:
                    
                    board[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box_index].add(num)

                    if backtrack(row, col + 1):  
                        return True

                    
                    board[row][col] = "."
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[box_index].remove(num)

            return False

        backtrack(0, 0)
