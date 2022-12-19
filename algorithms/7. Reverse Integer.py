class Solution(object):
    def reverse(self, x):
        is_negative = True if x < 0 else False
        str_x = str(x)
        if is_negative:
            str_x = str_x[1:]
        result = int(str_x[::-1]) * -1 if is_negative else int(str_x[::-1])
        if result < -2 ** 31 or result > 2 ** 31 - 1:
            return 0
        return result
        """
        :type x: int
        :rtype: int
        """