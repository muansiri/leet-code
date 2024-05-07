class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                s = strs[j]
                if i == len(s):
                    return ans
                if strs[0][0: i + 1] == s[0: i + 1]:
                    if j + 1 == len(strs):
                        ans = strs[0][0: i + 1]
                else:
                    break
        return ans

