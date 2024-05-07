class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }
        ans, i = 0, 0
        while i < len(s):
            c = s[i]
            if s[i: i + 2] in d and i + 1 < len(s):
                c += s[i + 1]
                i += 1
            ans += d[c]
            i += 1
        return ans

