class Solution(object):
    def longestPalindrome(self, s):
        result = ''
        n = len(s)
        for i in range(n):
            l, r, c = i, i, s[i]
            while (l > 0 and s[l - 1] == c):
                l -= 1

            while (r + 1 < n and s[r + 1] == c):
                r += 1

            for i in range(min(l, n - r - 1)):
                if (s[l - 1] == s[r + 1]):
                    l -= 1
                    r += 1
                else:
                    break
            if (len(result) < r - l + 1):
                result = s[l: r + 1]
        return result

        """
        :type s: str
        :rtype: str
        """