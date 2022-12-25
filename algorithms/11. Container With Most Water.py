class Solution(object):
    def maxArea(self, height):
        a, l, r = 0, 0, len(height) - 1
        while l != r:
            a = max(a, (r - l) * min(height[l], height[r]))
            if (height[r] < height[l]):
                r -= 1
            else:
                l += 1
        return a

        """
        :type height: List[int]
        :rtype: int
        """