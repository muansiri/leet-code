class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        c, y, z = 0, 0, x
        while z > 0:
            z = z // 10
            c += 1

        p = 10 ** (c - 1)
        z = x
        while z > 0:
            y += (z % 10) * p
            z //= 10
            p /= 10
        return x == y
        """
        :type x: int
        :rtype: bool
        """