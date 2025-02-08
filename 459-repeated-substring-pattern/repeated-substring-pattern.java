class Solution {
    public boolean repeatedSubstringPattern(String s) {
        String sub = s+s;
        return sub.substring(1,sub.length()-1).contains(s);
    }
}