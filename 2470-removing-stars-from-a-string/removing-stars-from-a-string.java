class Solution {
    public String removeStars(String s) {
        StringBuilder st = new StringBuilder();
        for(char c: s.toCharArray()){
            if(c != '*'){
                st.append(c);
            }else{
                st.deleteCharAt(st.length()-1);
            }
        }
        return st.toString();
    }
}