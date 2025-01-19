class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        num = set('123456789')

        def find(row_index,col_index):
            al = set()
            for i in board[row_index]:
                if i != "." and i not in al:
                    al.add(i)
            
            for i in range(9):
                d = board[i][col_index]
                if d != "." and d not in al:
                    al.add(d)
            
            box_pos_x = row_index // 3
            box_pos_y = col_index // 3
            for i in range(3):
                for j in range(3):
                    d = board[box_pos_x * 3 + i] [box_pos_y * 3 + j]
                    if d != '.' and d not in al:
                        al.add(d)
            
            return al

            
        
        def backtrack(row_index,col_index):
            if row_index == 9:
                return True
            if col_index == 9:
                return backtrack(row_index + 1, 0)
            
            if board[row_index][col_index] != ".":
                return backtrack(row_index, col_index +1)

            al = find(row_index, col_index)
            req = num - al

            for n in req:
                board[row_index][col_index] = n
                if backtrack(row_index, col_index +1):
                    return True
                board[row_index][col_index] = "."
            return False
        
        backtrack(0,0)
        
        