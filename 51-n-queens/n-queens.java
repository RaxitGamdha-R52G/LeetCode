class Solution {
    int num;
    char queen = 'Q';
    char[][] grid;
    List<List<String>> result = new ArrayList<>();
    private void solution(){
        List<String> temp = new ArrayList<>();

        for(int i = 0; i< num; i++){
            temp.add(new String(grid[i])); 
        }

        result.add(temp);
    }

    private boolean checkExist(int row, int col){
        // Check col;
        for(int i = 0; i< num; i++){
            if( grid[i][col] == queen){
                return false;
            }
        }

        // check left diagonal and right diagonal
        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (grid[i][j] == 'Q') return false;
        }
        for (int i = row, j = col; i >= 0 && j < num; i--, j++) {
            if (grid[i][j] == 'Q') return false;
        }
        return true;
    }

    private void backtrack(int row){
        if(row == num){
            solution();
            return;
        }
        for(int i = 0; i< num; i++){
            if(checkExist(row, i)){
                grid[row][i] = queen;
                backtrack(row+1);
                grid[row][i] = '.';
            }
        }


    }
    public List<List<String>> solveNQueens(int n) {
        num = n;
        grid = new char[n][n];
        for (char[] row : grid) {
            Arrays.fill(row, '.');
        }

        backtrack(0);
        return result;
    }
}