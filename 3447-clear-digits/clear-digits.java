class Solution {
    List<Character> arr =  new ArrayList<>();

    public String clearDigits(String s) {
        for(char c: s.toCharArray()){
            if(Character.isDigit(c)){
                arr.remove(arr.size()-1);
            }else{
                arr.add(c);
            }
        }
        StringBuilder result = new StringBuilder();
        arr.forEach((c) -> result.append(c));

        return result.toString();

    }
}