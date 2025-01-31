class Solution {
    public String decodeString(String s) {
        StringBuilder currstr = new StringBuilder();
        Stack<String> stack = new Stack<String>();
        Stack<Integer> numStack = new Stack<Integer>();
        int num = 0;


        for(char c: s.toCharArray()){
            if(Character.isDigit(c)){
                num = num* 10 + (c - '0');
            }else if(c == '['){
                numStack.push(num);
                stack.push(currstr.toString());
                currstr = new StringBuilder();
                num = 0;
            }
            else if(c == ']'){
                int rep = numStack.pop();
                StringBuilder temp = new StringBuilder(stack.pop());
                temp.append(currstr.toString().repeat(rep));
                currstr = temp;
            }else{
                currstr.append(c);

            }
        }

        return currstr.toString();
        
    }
}