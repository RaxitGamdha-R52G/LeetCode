class Solution {
    public int[] queryResults(int limit, int[][] queries) {
        Map<Integer, Integer> ballColor = new HashMap<>();
        Map<Integer, Integer> colorCount = new HashMap<>();
        int[] result = new int[queries.length];

        for (int i = 0; i < queries.length; i++) {
            int ball = queries[i][0];
            int color = queries[i][1];

            if(ballColor.getOrDefault(ball,-1) != color){

                if (ballColor.containsKey(ball)) {
                    int oldColor = ballColor.get(ball);
                        
                    colorCount.put(oldColor, colorCount.get(oldColor) - 1);

                    if (colorCount.get(oldColor) == 0) {
                        colorCount.remove(oldColor);
                    }
                }

                ballColor.put(ball, color);
                colorCount.put(color, colorCount.getOrDefault(color, 0) + 1);
            }

            result[i] = colorCount.size();
        }

        return result;

    }
}