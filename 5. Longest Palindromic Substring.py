class Solution(object):
    def longestPalindrome(self, s):
        if s == s[::-1]:
            return s

        result = ''
        length = len(s)
        for i in range(length):
            l, r = i, i
            while l - 1 >= 0 and s[l - 1] == s[i]:
                l = l - 1

            while r + 1 < length and s[r + 1] == s[i]:
                r = r + 1

            while l - 1 >= 0 and r + 1 < length and s[l - 1] == s[r + 1]:
                l = l - 1
                r = r + 1

            if r - l + 1 > len(result):
                result = s[l: r + 1]
        return result
