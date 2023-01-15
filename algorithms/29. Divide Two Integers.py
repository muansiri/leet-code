class Solution(object):
    def divide(self, dividend, divisor):
        is_negative = True if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) else False
        a, dividend, divisor = 0, abs(dividend), abs(divisor)

        while dividend - divisor >= 0:
            p = 0
            while dividend >= divisor << (p + 1) :
                p += 1
            dividend -= divisor << p
            a += 1 << p
        return max(-2 ** 31, -a) if is_negative else min(a, 2 ** 31 - 1)
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """