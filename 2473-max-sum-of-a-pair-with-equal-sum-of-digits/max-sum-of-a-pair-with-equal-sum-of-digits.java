class Solution {
    public int maximumSum(int[] nums) {
        Map<Integer,Integer> hs = new HashMap<>();
        int ans = -1;
        for(int num: nums){
            int sum = 0;
            int temp = num;
            while (temp > 0){
                sum += temp%10;
                temp /= 10;
            }
            if(hs.containsKey(sum)){
                ans = Math.max(ans, hs.get(sum)+num);
            }
            hs.merge(sum, num, Math::max);
        }

        return ans;
    }
}