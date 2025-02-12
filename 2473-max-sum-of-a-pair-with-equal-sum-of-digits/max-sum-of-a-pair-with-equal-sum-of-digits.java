class Solution {
    public int maximumSum(int[] nums) {
        // Map<Integer,Integer> hs = new HashMap<>();
        int[] arr = new int[100];
        int ans = -1;
        for(int num: nums){
            int sum = 0;
            int temp = num;
            while (temp > 0){
                sum += temp%10;
                temp /= 10;
            }
            // if(hs.containsKey(sum)){
            //     ans = Math.max(ans, hs.get(sum)+num);
            // }
            // hs.merge(sum, num, Math::max);
            if(arr[sum]!= 0){
                ans = Math.max(ans,arr[sum]+num);
            }
            arr[sum] = Math.max(arr[sum],num);
        }

        return ans;
    }
}