class Solution {
    public int maxFreeTime(int eventTime, int k, int[] startTime, int[] endTime) {
        int n = endTime.length;
        
        int[] diff = new int[n + 1];
        int index = 0;

        diff[index++] = startTime[0];

        for (int i = 1; i < n; i++) {
            int freeTime = startTime[i] - endTime[i - 1];
            diff[index++] = freeTime;
        }

        if (eventTime > endTime[n - 1]) {
            diff[index] = eventTime - endTime[n - 1];
        }

        int window_size = Math.min(k+1, diff.length);
        int[] prefix = new int[diff.length + 1];

        for (int i = 0; i < diff.length; i++) {
            prefix[i + 1] = diff[i] + prefix[i];
        }

        int maxTime = 0;
        for (int i = 0; i < prefix.length - window_size; i++) {
            int time = prefix[i + window_size] - prefix[i];
            maxTime = Math.max(maxTime, time);
        }
        
        return maxTime;

    }
}