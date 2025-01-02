class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Each Row
        rows = []

        #Each Column
        columns = []

        #Each Box
        box = [[] for i in range(9)]
        q = 0
        c_arr = -1
        
        for i in range(9):
            temp_r = [] # For rows
            temp_c = [] # For columns

            if i % 3 == 0: #For Boxes
                c_arr += 1

            for j in range(9):
                t_r = board[i][j] 
                if t_r != ".":
                    temp_r.append(t_r)

                    q = j//3
                    box[q+3*c_arr].append(board[i][j])

                t_c = board[j][i]
                if t_c != ".":
                    temp_c.append(t_c)

            rows.append(temp_r)
            columns.append(temp_c)
        

        merged_arr = [rows, columns, box]
        
        for arr in merged_arr:
            for i in arr:
                if not self.check(i):
                    return False
        
        return True
    
    def check(self,arr):
        arr_set_len = len(set(arr))
        arr_arr_len = len(arr)
        
        return arr_set_len == arr_arr_len
        
        
        

            

        