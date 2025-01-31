class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder st = new StringBuilder();
        int i = 0;
        boolean cont = true, s1, s2;
        while(cont){
            s1 = false;
            s2 = false;
            if (i<word1.length()){
                s1 = true;
                st.append(word1.charAt(i));
            }
            if (i<word2.length()){
                s2 = true;
                st.append(word2.charAt(i));
            }
            cont = s1 || s2;
            i++;
        }

        return st.toString();
    }
}