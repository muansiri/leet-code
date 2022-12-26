class Solution(object):
    def longestCommonPrefix(self, strs):
        a = strs[0]
        for i in range(1, len(strs)):
            current_str = strs[i]
            current_n = len(current_str)
            if current_n == 0:
                return ""
            for j in range(current_n):
                if j == len(a) or a[j] != current_str[j]:
                    a = current_str[0: j]
                    break
                elif j == current_n - 1:
                    a = current_str[0:]
        return a


        """
        :type strs: List[str]
        :rtype: str
        """