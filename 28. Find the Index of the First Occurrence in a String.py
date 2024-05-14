class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenght_needle = len(needle)
        length_haystack = len(haystack)
        for i in range(length_haystack - lenght_needle + 1):
            if needle == haystack[i: i + lenght_needle]:
                return i
        return -1
