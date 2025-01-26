class Solution {
    public int countAsterisks(String s) {
        boolean check = false;
        int res = 0;
        for(char c: s.toCharArray()){
            if(c == '|'){
                check = !check;
            }else if(c == '*' && !check){
                res++;
            }
        }
        
        return res;
    }
}