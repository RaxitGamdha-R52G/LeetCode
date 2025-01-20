class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i = 0
        length = len(tickets)
        seconds = 0
        while tickets[k] != 0:
            if i == length:
                i = 0
            if tickets[i] != 0:
                tickets[i] -= 1
                seconds += 1
            i+= 1

        return seconds