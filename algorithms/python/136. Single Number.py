class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = {}
        for num in nums:
            if num not in ans:
                ans[num] = True
            else:
                del ans[num]
        ans = list(ans.keys())
        return ans[0]
