class Solution {
    private int n;
    private int result = 0;

    private void backtrack(int curr, int[] arr, int sum){
        if(curr == n){
            result += sum;
            return;
        }

        backtrack(curr+1, arr, sum ^ arr[curr]);
        backtrack(curr+1, arr, sum);
    }

    public int subsetXORSum(int[] nums) {
        n = nums.length;
        backtrack(0, nums, 0);
        return result;
    }
}