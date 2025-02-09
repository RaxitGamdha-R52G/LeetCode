class Solution {
    private Set<Character>[] row = new HashSet[9];
    private Set<Character>[] col = new HashSet[9];
    private Set<Character>[] box = new HashSet[9];
    private char[][] grid;

    private boolean backtrack(int i, int j) {
        if (i == 9) {
            return true;
        }
        if (j == 9) {
            return backtrack(i + 1, 0);
        }
        if (grid[i][j] != '.') {
            return backtrack(i, j + 1);
        }

        int box_index = (i / 3) * 3 + (j / 3);
        for (char c = '1'; c <= '9'; c++) {
            if (!row[i].contains(c) && !col[j].contains(c) && !box[box_index].contains(c)) {
                grid[i][j] = c;
                row[i].add(c);
                col[j].add(c);
                box[box_index].add(c);

                if (backtrack(i, j + 1)) {
                    return true;
                }

                grid[i][j] = '.';
                row[i].remove(c);
                col[j].remove(c);
                box[box_index].remove(c);
            }
        }
        return false;
    }

    public void solveSudoku(char[][] board) {
        grid = board;
        for (int i = 0; i < 9; i++) {
            row[i] = new HashSet<>();
            col[i] = new HashSet<>();
            box[i] = new HashSet<>();
        }

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    continue;
                }
                char num = board[i][j];
                row[i].add(num);
                col[j].add(num);
                box[(i / 3) * 3 + (j / 3)].add(num);
            }
        }
        backtrack(0, 0);
    }
}