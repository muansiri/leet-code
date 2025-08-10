class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def recursive(s, l, r):
            if n == l and n == r:
                ans.append(s)
                return
            if l < n:
                recursive(s + "(", l + 1, r)
            if r < l:
                recursive(s + ")", l, r + 1)
        recursive("", 0, 0)
        return ans
