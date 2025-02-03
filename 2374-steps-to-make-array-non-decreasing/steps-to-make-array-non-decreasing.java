class Solution {
    public int totalSteps(int[] nums) {
        Stack<int[]> stack = new Stack<>();
        int maxSteps = 0;

        for(int c: nums){
            int steps = 0;

            while(!stack.isEmpty() && stack.peek()[0] <= c){
                steps = Math.max(steps, stack.pop()[1]);
            }
            steps = stack.isEmpty()?0:steps+1;
            maxSteps = Math.max(steps, maxSteps);
            stack.push(new int[] {c, steps});
        }

        return maxSteps;
    }
}