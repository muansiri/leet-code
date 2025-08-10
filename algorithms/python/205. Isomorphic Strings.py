class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        z = zip(s, t)
        mapS, mapT = {}, {}
        for d in z:
            a, b = d
            if a in mapS and mapS[a] != b:
                return False
            if b in mapT and mapT[b] != a:
                return False
            mapS[a] = b
            mapT[b] = a
        return True
