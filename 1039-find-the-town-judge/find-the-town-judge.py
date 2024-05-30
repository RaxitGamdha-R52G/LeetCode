class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        for i,j in trust:
            indegree[j] += 1
            outdegree[i] += 1
        
        for node,in_node in indegree.items():
            if in_node == n-1 and outdegree[node] == 0:
                return node
        
        return -1