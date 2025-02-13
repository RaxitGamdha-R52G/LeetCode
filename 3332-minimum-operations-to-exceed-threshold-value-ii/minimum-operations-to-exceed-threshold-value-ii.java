class Solution {
    public int minOperations(int[] nums, int k) {
        PriorityQueue<Long> pq = new PriorityQueue<>();
        for (int num : nums) {
            pq.add((long)num);
        }

        int result = 0;
        
        while (pq.size() > 1 && pq.peek() < k) {
            long num1 = pq.poll();
            long num2 = pq.poll();

            long newNum = num1 * 2 + num2;
            pq.add(newNum);
            result++;
        }
        
        return result;
    }
}
