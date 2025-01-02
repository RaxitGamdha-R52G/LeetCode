class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Each Row
        for i in range(9):
            temp = []
            for j in board[i]:
                if j != ".":
                    temp.append(j)
            d = Counter(temp)
            if not self.check(d):
                return False

        #Each Column
        for j in range(9):
            temp = []
            for i in range(9):
                if board[i][j] != ".":
                    temp.append(board[i][j])
            d = Counter(temp)
            if not self.check(d):
                return False
        
        #Each Box
        temp = [[] for i in range(9)]
        q = 0
        c_arr = -1
        for i in range(9):
            if i % 3 == 0:
                c_arr += 1
            for j in range(9):
                if board[i][j] != ".":
                    q = j//3
                    temp[q+3*c_arr].append(board[i][j])
        
        print(temp)
        
        for i in temp:
            d = Counter(i)
            if not self.check(d):
                return False
        
        return True
    
    def check(self,d):
        for val in d.values():
            if val > 1:
                return False
        return True
        
        
        

            

        