class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        
        StringBuilder st = new StringBuilder();
        int index = 0;
        String temp = strs[0];
        
        while (true) {
            for (String c : strs) {
                if (index >= c.length() || c.charAt(index) != temp.charAt(index)) {
                    return st.toString();
                }
            }
            st.append(temp.charAt(index));
            index++;
        }
    }
}