class Solution {
    public int tupleSameProduct(int[] nums) {
        int n = nums.length;
        Map<Integer,Integer> hs  = new HashMap<>();
        int result = 0;

        for(int i =0; i< n-1;i++){
            for(int j = i+1;j<n;j++){
                int product = nums[i] * nums[j];
                hs.put(product, hs.getOrDefault(product,0)+1);
            }
        }

        for(int freq: hs.values()){
            if(freq > 1){
                result += freq*(freq-1)/2 * 8;
            }
        }

        return result;
    }
}