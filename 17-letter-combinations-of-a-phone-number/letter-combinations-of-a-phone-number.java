class Solution {
    private String[] arr = new String[8];
    private List<String> result = new ArrayList<>();
    private String num;

    private void backtrack(StringBuilder temp, int curr){
        if(curr == num.length()){
            result.add(temp.toString());
            return;
        }

        int c = Character.getNumericValue(num.charAt(curr));
        for(char ch: arr[c-2].toCharArray()){
            temp.append(ch);
            backtrack(temp, curr+1);
            temp.deleteCharAt(temp.length()-1);
        }
    }

    public List<String> letterCombinations(String digits) {
        if(digits.equals("")) return new ArrayList<>();
        arr[0] = "abc";
        arr[1] = "def";
        arr[2] = "ghi";
        arr[3] = "jkl";
        arr[4] = "mno";
        arr[5] = "pqrs";
        arr[6] = "tuv";
        arr[7] = "wxyz";

        num = digits;
        backtrack(new StringBuilder(), 0);
        return result;
    }
}