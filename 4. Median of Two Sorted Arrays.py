class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        length = len(nums)
        middle = length // 2
        if length % 2 == 0:
            return (nums[middle] + nums[middle - 1]) / 2.0
        else:
            return float(nums[middle])
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """