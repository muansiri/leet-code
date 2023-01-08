class Solution(object):
    def isValid(self, s):
        a, d = [], {'}': '{', ')': '(', ']': '['}
        for c in s:
            if c in d and len(a) and a[-1] == d[c]:
                a.pop()
            else:
                a.append(c)
        return len(a) == 0
        """
        :type s: str
        :rtype: bool
        """