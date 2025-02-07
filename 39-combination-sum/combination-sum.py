class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(i, target):
            if target == 0:
                result.append(path.copy())
                return
            
            if(i >= len(candidates)):return

            diff = target - candidates[i]

            if(diff >= 0):
                path.append(candidates[i])
                backtrack(i,diff)
                path.pop()

            backtrack(i+1, target)

        backtrack(0, target)
        return result