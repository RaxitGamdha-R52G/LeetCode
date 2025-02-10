class Solution {
    int num;
    int result = 0;
    boolean[][] grid;

    private boolean check(int row, int col){
        for(int i = 0; i < num; i++){
            if(grid[i][col]) return false;
        }

        for(int i = row, j = col; i >= 0 && j >= 0; i--, j--){
            if(grid[i][j]) return false;
        }
        
        for(int i = row, j = col; i >= 0 && j < num; i--, j++){
            if(grid[i][j]) return false;
        }

        return true;

    }

    private void backtrack(int row){
        if(row == num){
            result++;
            return;
        }

        for(int i = 0; i < num; i++){
            if(check(row, i)){
                grid[row][i] = true;
                backtrack(row + 1);
                grid[row][i] = false;
            }
        }
    }

    public int totalNQueens(int n) {
        if(n == 2 || n == 3) return 0;
        if(n == 1) return 1;
        if(n == 4) return 2;
        num = n;
        grid = new boolean[n][n];
        backtrack(0);
        return result;
    }
}