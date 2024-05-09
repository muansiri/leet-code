class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        length = len(nums)
        ans = []
        for i in range(length):
            if i != 0 and nums[i] == nums[i -1]:
                continue
            for j in range(i + 1, length):
                if j != i + 1 and nums[j] == nums[j -1]:
                    continue

                l, r = j + 1, length - 1
                while l < r:
                    sums = nums[i] + nums[j] + nums[l] + nums[r]
                    if sums > target:
                        r -= 1
                    elif sums < target:
                        l += 1
                    else:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l -1] and l < r:
                            l += 1
        return ans
