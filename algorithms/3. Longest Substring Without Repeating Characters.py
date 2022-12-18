class Solution(object):
    def lengthOfLongestSubstring(self, s):
        result = 0
        left = 0
        obj = {}
        for i in range(len(s)):
            c = s[i]
            if c in obj and obj[c] + 1 > left:
                left = obj[c] + 1
            obj[c] = i
            result = max(result, i - left + 1)
        return result

        """
        :type s: str
        :rtype: int
        """