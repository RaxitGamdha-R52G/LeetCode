class Solution {
    public String removeOccurrences(String s, String part) {
        // if(!s.contains(part)){
        //     return s;
        // }
        // s = s.replaceFirst(part,"");
        // return removeOccurrences(s, part);
        char[] targetArr = part.toCharArray();
        char[] stack = new char[s.length()];
        int stackSize = 0;
        char t_Char = targetArr[targetArr.length-1];

        for(char c_Char: s.toCharArray()){
            stack[stackSize++] = c_Char;

            if(t_Char == c_Char && stackSize >= targetArr.length){
                int i = stackSize-1, j = targetArr.length -1;
                while(j>=0 && stack[i] == targetArr[j]){
                    i--;
                    j--;
                }

                if(j < 0){
                    stackSize = i+1;
                }
            }
        }

        return new String(stack, 0, stackSize);
    }
}