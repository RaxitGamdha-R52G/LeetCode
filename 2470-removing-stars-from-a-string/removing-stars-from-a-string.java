class Solution {
    public String removeStars(String s) {
        Stack<Character> stack=new Stack<>();
        StringBuilder newStr=new StringBuilder();
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)!='*'){
                stack.push(s.charAt(i));
            }
            else{
                stack.pop();
            }
        }

        while(!stack.isEmpty()){
            newStr.append(stack.pop());
        }

        newStr.reverse();

        return newStr.toString();


    }
}