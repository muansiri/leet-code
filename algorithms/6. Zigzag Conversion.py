from collections import defaultdict

class Solution(object):
    def convert(self, s, numRows):
        mode = 'D'
        i = 0
        d = defaultdict(lambda: '')
        for c in s:
            d[i] += c
            if mode == 'D':
                i += 1
            elif mode == 'U':
                i -= 1

            if i == numRows:
                mode = 'U'
                i = max(0, numRows - 2)
            elif i == -1:
                mode = 'D'
                i = min(1, numRows -1)
            pass
        result = ''
        for i in range(numRows):
            result += d[i]
        return result
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """