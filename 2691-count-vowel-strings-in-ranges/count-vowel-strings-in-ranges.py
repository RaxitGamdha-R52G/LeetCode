class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        w = len(words)
        result = []
        match = lambda x: x.lower() in ('a','e','i','o','u')
        temp = [0]
        for i in range(w):
            if words[i] != "" and match(words[i][0]) and match(words[i][-1]):
                r = temp[-1]+1
            else:
                r = temp[-1]
            temp.append(r)

        for start,stop in queries:
            result.append(temp[stop+1] - temp[start])
        return result
        