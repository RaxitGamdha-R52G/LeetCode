class Solution {
    public long countBadPairs(int[] nums) {
        Map<Integer, Integer> hs = new HashMap<>();
        long totalPair = 0, goodPair = 0;
        int n = nums.length;

        for(int i = 0; i< n; i++){
            int diff = nums[i] - i;
            goodPair += hs.getOrDefault(diff, 0);
            hs.merge(diff, 1, Integer::sum);
        }
        
        totalPair = (long) n*(n-1)/2;

        return totalPair- goodPair;
    }
}