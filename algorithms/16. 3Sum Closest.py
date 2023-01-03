class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        a = nums[0] + nums[1] + nums[2]
        for i, v in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = v + nums[l] + nums[r]
                if abs(threeSum - target) < abs(a - target):
                    a = threeSum

                if threeSum > target:
                    r -= 1
                elif threeSum < target:
                    l += 1
                elif threeSum == target:
                    return threeSum
        return a
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """