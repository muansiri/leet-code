class Solution(object):
    def removeElement(self, nums, val):
        a = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[a] = nums[i]
            a += 1
        return a
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """