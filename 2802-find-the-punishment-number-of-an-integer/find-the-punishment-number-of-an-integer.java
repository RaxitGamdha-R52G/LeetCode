class Solution {
    private boolean canPartition(String numberStr, int pos, int target) {
        if (target == 0 && pos == numberStr.length()) return true;
        if (target < 0 || pos == numberStr.length()) return false;

        int currentNum = 0;
        for (int i = pos; i < numberStr.length(); i++) {
            currentNum = currentNum * 10 + (numberStr.charAt(i) - '0');
            if (canPartition(numberStr, i + 1, target - currentNum)) return true;
        }
        return false;
    }

    public int punishmentNumber(int n) {
        int totalSum = 0;
        for (int num = 1; num <= n; num++) {
            int squaredValue = num * num;
            if (canPartition(String.valueOf(squaredValue), 0, num)) {
                totalSum += squaredValue;
            }
        }
        return totalSum;
    }
}
