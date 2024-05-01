class Solution(object):
    def twoSum(self, nums, target):
        value_index = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in value_index:
                return [min(value_index[diff], index), max(value_index[diff], index)]
            value_index[value] = index
        return []

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
