class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        HashMap<Character, Integer> hs = new HashMap<Character, Integer>();
        HashMap<Character, Integer> hs1 = new HashMap<Character, Integer>();

        for(char c: s1.toCharArray()){
            hs.put(c,hs.getOrDefault(c,0)+1);
        }
        for(char c: s2.toCharArray()){
            hs1.put(c,hs1.getOrDefault(c,0)+1);
        }

        if(!hs.equals(hs1)){
            return false;
        }
        
        int count = 0;
        for(int i = 0; i< s1.length(); i++){
            if(s1.charAt(i) != s2.charAt(i)){
                count++;
            }
        }

        if(count %2 ==1 || count /2 > 1){
            return false;
        }
        return true;

    }
}