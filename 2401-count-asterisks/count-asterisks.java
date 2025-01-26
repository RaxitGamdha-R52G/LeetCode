class Solution {
    public int countAsterisks(String s) {
        boolean check = false;
        int res = 0;
        for(int i = 0; i< s.length();i++){
            char c = s.charAt(i);
            if(c == '|'){
                check = !check;
            }else if(c == '*' && !check){
                res++;
            }
        }
        
        return res;
    }
}