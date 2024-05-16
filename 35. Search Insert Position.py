class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            i = (l + r) // 2
            if target == nums[i]:
                return i
            elif target < nums[i]:
                r = i - 1
            elif target > nums[i]:
                l = i + 1
        return l
