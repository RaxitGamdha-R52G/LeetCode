class Solution {
    public int hammingWeight(int n) {
        int ar[] = new int[32];
        int i = 0;
        while(n> 0){
            ar[i++] = n % 2;
            n /= 2;
        }
        int sum = 0;
        for(int j = 0;j<i;j++){
            if( ar[j] == 1){
                sum++;
            }
        }
        return sum;
    }
}