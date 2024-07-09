class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        k = customers[0][0]
        result = []
        for i in customers:
            if k < i[0]:
                k = i[0]
            k += i[1]
            result.append(k-i[0])
        return sum(result) / len(result)      