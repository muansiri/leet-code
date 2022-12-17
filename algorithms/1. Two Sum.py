class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, v in enumerate(nums):
          diff = target - v
          if diff in d:
            return [d[diff], i]

          d[v] = i

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """