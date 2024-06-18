class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        length = len(columnTitle)
        for i in range(length):
            c = columnTitle[length - i - 1]
            ans += (ord(c) - 64) * 26**i
        return ans
