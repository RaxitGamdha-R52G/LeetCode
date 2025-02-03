class Solution {
    public int timeRequiredToBuy(int[] tickets, int k) {
        int length = tickets.length, i = 0, seconds = 0;

        while(tickets[k] != 0){
            if(i == length){
                i = 0;
            }

            if(tickets[i]  != 0){
                tickets[i]--;
                seconds++;
            }
            i++;
        }

        return seconds;
        
        
    }
}