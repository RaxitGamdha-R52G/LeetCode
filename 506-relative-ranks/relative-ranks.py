class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        import copy
        ranks = copy.copy(score)
        ranks.sort(reverse = True)
        result = [0] * len(score)

        for i in range(len(ranks)):
            index = score.index(ranks[i])
            if i == 0:
                result[index] = 'Gold Medal'
            elif i == 1:
                result[index] = 'Silver Medal'
            elif i == 2:
                result[index] = 'Bronze Medal'
            else:
                result[index] = str(i + 1)
        return result

