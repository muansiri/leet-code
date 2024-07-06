class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        e = {}
        for i in range(len(s)):
            c = s[i]
            if c in d and t[i] != d[c]:
                return False
            d[c] = t[i]

            c = t[i]
            if c in e and s[i] != e[c]:
                return False
            e[c] = s[i]
        return True

