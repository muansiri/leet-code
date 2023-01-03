class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        a = []
        print('nums', nums)
        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = v + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    a.append([v, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return a

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """