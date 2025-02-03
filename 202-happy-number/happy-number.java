class Solution {
    public boolean isHappy(int n) {
        // Solution 1
        // HashSet<Integer> hs = new HashSet<Integer>();
        // while(n > 1){
        //     int sum = 0;
        //     while(n > 0){
        //         int d = n % 10;
        //         n /= 10;
        //         sum += Math.pow(d,2);
        //     }
        //     if (hs.contains(sum)){
        //         return false;
        //     }
        //     hs.add(sum);
        //     n = sum;
        // }
        // return true;

        // Solution 2
        if(n == 1 || n == 7){
            return true;
        }else if(n < 10){
            return false;
        }
        int sum = 0;
        while (n > 0){
            int d = n %10;
            n /= 10;
            sum += Math.pow(d,2);
        }
        return isHappy(sum);
    }
}