class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        current_row = 0
        result = [""] * numRows
        down = False
        for c in s:
            result[current_row] += c
            if current_row == 0 or current_row == numRows - 1:
                down = not down
            current_row += 1 if down else -1
        return "".join(result)
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
