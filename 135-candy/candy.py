class Solution:
    def candy(self, ratings: List[int]) -> int:
        L = len(ratings)
        cand = [1 for i in range(L)]
        for i in range(1,L):
            if ratings[i] > ratings[i-1]:
                cand[i] = cand[i-1]+1
        for i in range(L-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                cand[i] = max(cand[i],cand[i+1]+1)
        
        return sum(cand)
        