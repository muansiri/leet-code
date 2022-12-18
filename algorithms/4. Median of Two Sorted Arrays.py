class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        n = len(nums)
        index = int(n / 2)
        if n % 2 == 0:
            return (nums[index - 1] + nums[index]) / 2.0
        else:
            return nums[index]
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """