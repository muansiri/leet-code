class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        for c in s:
            if stack and stack[-1] == d.get(c):
                stack.pop(len(stack) - 1)
            else:
                stack.append(c)
        return len(stack) == 0