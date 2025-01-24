class Solution {
    public static void swap(int[] nums, int st, int end){
        for(int i = 0; i < (end - st) /2;i++){
            int temp = nums[st + i];
            nums[st + i] = nums[end - i -1];
            nums[end - i- 1] = temp;
        }
        return;
    }

    public void rotate(int[] nums, int k) {
        k %= nums.length;
        if(k == 0) return;
        swap(nums, 0, nums.length);
        swap(nums, 0, k);
        swap(nums, k, nums.length);

        return;
    }
}