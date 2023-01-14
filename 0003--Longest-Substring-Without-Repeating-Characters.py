class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        char_set = set()
        for end in range(len(s)):
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            char_set.add(s[end])
            max_length = max(max_length, end - start + 1)
        return max_length

    def lengthOfLongestSubstring(s: str) -> int:
        start = 0
        max_length = 0
        char_map = {}
        for end in range(len(s)):
            if s[end] in char_map:
                start = max(start, char_map[s[end]] + 1)
            char_map[s[end]] = end
            max_length = max(max_length, end - start + 1)
        return max_length
