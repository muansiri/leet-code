class Solution(object):
    def generateParenthesis(self, n):
        def dfs(l, r, s):
            if len(s) == n * 2:
                a.append(s)

            if l < n:
                dfs(l + 1, r, s + '(')

            if r < l:
                dfs(l, r + 1, s + ')')
        a = []
        dfs(0, 0, '')
        return a
        """
        :type n: int
        :rtype: List[str]
        """
