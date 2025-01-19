class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_count = Counter(words)
        word_length = len(words[0])
        substring_length = word_length * len(words)
        result = []

        for i in range(word_length):
            left = i
            right = i
            count = 0
            window_map = Counter()

            while right + word_length <= len(s):
                word = s[right:right + word_length]
                right += word_length

                if word in word_count:
                    window_map[word] += 1
                    count += 1

                    while window_map[word] > word_count[word]:
                        left_word = s[left:left + word_length]
                        window_map[left_word] -= 1
                        count -= 1
                        left += word_length

                    if count == len(words):
                        result.append(left)

                else:
                    window_map.clear()
                    count = 0
                    left = right

        return result
        