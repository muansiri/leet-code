class Solution(object):
    def lengthOfLongestSubstring(self, s):
        result = 0
        start = 0
        data = {}
        for i in range(0, len(s)):
            c = s[i]
            if c in data and data[c] >= start:
                start = data[c] + 1
            else:
                result = max(result, i - start + 1)
            data[c] = i
        return result
        """
        :type s: str
        :rtype: int
        """
