class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = Counter(s)
        stack = []
        v = set()

        for ch in s:
            c[ch] -= 1
            if ch in v:
                continue

            while stack and stack[-1] >= ch:
                temp = stack[-1]
                if c[temp] > 0:
                    stack.pop()
                    v.remove(temp)
                else:
                    break
            v.add(ch)
            stack.append(ch)
        
        return "".join(stack)
                