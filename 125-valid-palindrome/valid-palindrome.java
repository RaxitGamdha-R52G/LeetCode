class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder st = new StringBuilder();
        for(char c: s.toCharArray()){
            if (Character.isLetterOrDigit(c)){
                st.append(Character.toLowerCase(c));
            }
        }
        s = st.toString();

        int left = 0;
        int right = s.length() -1;
        while(left<right){
            if(s.charAt(left) != s.charAt(right)){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}