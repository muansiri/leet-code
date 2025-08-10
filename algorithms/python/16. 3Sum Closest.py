class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        answer = 2**31 - 1
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i -1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                sum_nums = nums[i] + nums[l] + nums[r]
                if abs(sum_nums - target) < abs(answer - target):
                    answer = sum_nums
                if sum_nums > target:
                    r -= 1
                elif sum_nums < target:
                    l += 1
                else:
                    return target
        return answer
