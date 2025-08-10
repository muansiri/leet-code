class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def recursive(current_step, memo):
            if current_step <= 2:
                return current_step
            if current_step not in memo:
                memo[current_step] = recursive(current_step - 1, memo) + recursive(current_step - 2, memo)
            return memo[current_step]
        return recursive(n, memo)
