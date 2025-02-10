class Solution {
    private int upTo;
    private int num;
    private List<Integer> path = new ArrayList<>();
    private List<List<Integer>> result = new ArrayList<>();

    private void backtrack(int val, int curr){
        if( curr == upTo){
            result.add(new ArrayList(path));
            return;
        }

        if (val <= num){
            path.add(val);
            backtrack(val+1, curr+1);
            path.remove(path.size()-1);
            backtrack(val+1, curr);
        }
    }

    public List<List<Integer>> combine(int n, int k) {
        upTo = k;
        num = n;
        backtrack(1,0);
        return result;
    }
}