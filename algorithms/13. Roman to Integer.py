class Solution(object):
    def romanToInt(self, s):
        a = 0
        d = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }
        for i in range(len(s)):
            if s[i: i + 2] in d:
                a += s[i: i + 2]
                i += 1
            else:
                a += s[i: i + 1]
        return a
        """
        :type s: str
        :rtype: int
        """