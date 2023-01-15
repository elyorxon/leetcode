import operator


class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "#".join(f"^{s}$")
        n = len(t)
        p = [0] * n
        c = 0
        r = 0
        for i in range(1, n - 1):
            p[i] = (r > i) and min(r - i, p[2 * c - i])
            # attempt to expand the palindrome centered at i
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1
                # update the center and rightmost boundary of the palindrome
                if i + p[i] > r:
                    c, r = i, i + p[i]
        # find the center and length of the longest palindrome
        center, length = max(enumerate(p), key=operator.itemgetter(1))
        return s[(center - length) // 2: (center + length) // 2]


############# Second solution ##############################
def longestPalindrome(s: str) -> str:
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    ans = ""
    max_len = 0

    # every string with one character is a palindrome
    for i in range(n):
        dp[i][i] = True
        ans = s[i]
        max_len = 1

    for start in range(n - 1, -1, -1):
        for end in range(start + 1, n):
            # case 1: string with two characters
            if s[start] == s[end] and end - start == 1:
                dp[start][end] = True
            # case 2: string with more than two characters
            elif s[start] == s[end] and dp[start + 1][end - 1]:
                dp[start][end] = True
            if dp[start][end]:
                if end - start + 1 > max_len:
                    max_len = end - start + 1
                    ans = s[start:end + 1]
    return ans
