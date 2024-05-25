class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        count_m = 0
        count_n = 0
        copy_nums1 = nums1.copy()

        for i in range(m + n):
            if count_n == n or (count_m < m and copy_nums1[count_m] < nums2[count_n]):
                nums1[i] = copy_nums1[count_m]
                count_m += 1
            else:
                nums1[i] = nums2[count_n]
                count_n += 1
        """
        Do not return anything, modify nums1 in-place instead.
        """
