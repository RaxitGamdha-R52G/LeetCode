class Solution {
    private int n;
    private List<List<Integer>> result = new ArrayList<>();
    private List<Integer> path = new ArrayList<>();

    private void backtrack(int curr,int[] arr){
        if(n == curr){
            result.add(new ArrayList(path));
            return;
        }

        path.add(arr[curr]);
        backtrack(curr+1, arr);
        path.remove(path.size()-1);
        backtrack(curr+1, arr);
    }

    public List<List<Integer>> subsets(int[] nums) {
        n = nums.length;
        backtrack(0, nums);
        return result;
    }
}