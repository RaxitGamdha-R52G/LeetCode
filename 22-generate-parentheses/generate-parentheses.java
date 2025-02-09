class Solution {
    private List<String> result = new ArrayList<>();
    private int num;
    private void backtrack(StringBuilder temp, int open, int close){
        if(temp.length() == 2*num){
            result.add(temp.toString());
            return;
        }

        if(open < num){
            temp.append('(');
            backtrack(temp,open+1, close);
            temp.deleteCharAt(temp.length()-1);
        }
        if(close < open){
            temp.append(')');
            backtrack(temp,open, close+1);
            temp.deleteCharAt(temp.length()-1);
        }
    }

    public List<String> generateParenthesis(int n) {
        num = n;
        backtrack(new StringBuilder(), 0, 0);
        return result;
    }
}