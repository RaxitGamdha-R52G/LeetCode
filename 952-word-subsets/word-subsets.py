class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        w2 = Counter()
        for s in words2:
            b = Counter(s)
            for key in b:
                if w2[key] <= b[key]:
                    w2[key] = b[key]
            

        result = []
        for w1 in words1:
            flag = True
            c = Counter(w1)
            for key in w2:
                if c[key] < w2[key]:
                    flag = False
                    break
            if flag:
                result.append(w1)
        
        return result

    