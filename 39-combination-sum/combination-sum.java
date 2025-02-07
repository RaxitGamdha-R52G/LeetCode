class Solution {
    // private List<List<Integer>> result = new ArrayList<List<Integer>>();
    // private void backtrack(int[] candidates, int target, List<Integer> path, int start ){
    //     if(target == 0){
    //         // Collections.sort(path);
    //         // if(!result.contains(path))result.add(path);
    //         result.add(new ArrayList<>(path));
    //         return;
    //     }

    //     // for (int i = start; i < candidates.length; i++){
    //     //     int diff = target - candidates[i];
    //     //     // if(diff >= 0){
    //     //     //     List<Integer> temp = new ArrayList<Integer>(path);
    //     //     //     temp.add(num);
    //     //     //     backtrack(candidates, diff, temp);
    //     //     // }
    //     //     if(diff >= 0){
    //     //         path.add(candidates[i]);
    //     //         backtrack(candidates, diff, path, i);
    //     //         path.remove(path.size()-1);
    //     //     }
    //     }
    // }

    private List<List<Integer>> result = new ArrayList<>();
    private List<Integer> path = new ArrayList<>();
    private void backtrack(int[] candidates, int target, int i ){
        if( target == 0){
            result.add(new ArrayList<>(path));
            return;
        }

        if (i >= candidates.length) return;


        int diff = target - candidates[i];
        if(diff >= 0){
            path.add(candidates[i]);
            backtrack(candidates, diff, i);
            path.remove(path.size()-1);
        }
        backtrack(candidates, target, i+1);

        }
    

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        // backtrack(candidates,target, new ArrayList<>(), 0);
        backtrack(candidates,target, 0);
        return result;
    }
}