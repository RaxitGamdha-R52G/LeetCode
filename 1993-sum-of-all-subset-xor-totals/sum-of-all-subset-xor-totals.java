class Solution {
    private int n;
    private List<Integer> path = new ArrayList<>();
    private int result = 0;

    private void calc(){
        int xor = 0;
        for(int num: path){
            xor ^= num;
        }
        result += xor;
    }

    private void backtrack(int curr, int[] arr){
        if(curr == n){
            calc();
            return;
        }

        path.add(arr[curr]);
        backtrack(curr+1, arr);
        path.remove(path.size()-1);
        backtrack(curr+1, arr);
    }

    public int subsetXORSum(int[] nums) {
        n = nums.length;
        backtrack(0, nums);
        return result;
    }
}