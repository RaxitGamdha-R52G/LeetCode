class Solution {
    public int majorityElement(int[] nums) {
        if(nums.length == 0) return -1;
        int maj = nums[0];
        int count = 1;

        for(int i = 1; i < nums.length; i++){
            if (maj == nums[i]){
                count++;
            }else{
                count--;
            }

            if (count == 0){
                maj = nums[i];
                count = 1;
            }
        }

        return maj;
        
    }
}