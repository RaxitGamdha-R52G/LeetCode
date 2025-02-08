class Solution {
    private boolean check(String s, String str){
        return str.repeat(s.length()/str.length()).equals(s);
    }

    public boolean repeatedSubstringPattern(String s) {
        // String sub = s+s;
        // return sub.substring(1,sub.length()-1).contains(s);
        int slen = s.length();
        for(int i = 1; i*i <= slen; i++){
            if(slen %i == 0){
                if(i != slen && check(s, s.substring(0,i))) return true;
                int len2 = slen/i;
                if(len2 != slen && check(s, s.substring(0,len2))) return true;
            }
        }

        return false;
    }
}