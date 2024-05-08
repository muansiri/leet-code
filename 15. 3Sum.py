class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans, f_nums = [], []
        d, k = {}, {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
            if d[num] <= 3:
                f_nums.append(num)
        length = len(f_nums)
        for i in range(length):
            for j in range(i + 1, length):
                diff = (f_nums[i] + f_nums[j]) * -1
                if diff in d:
                    numbers = [f_nums[i], f_nums[j]]
                    count = 1
                    if diff == f_nums[i]:
                        count += 1
                    if diff == f_nums[j]:
                        count += 1
                    if d[diff] >= count:
                        sorted_ans = sorted([f_nums[i], f_nums[j], diff])
                        key = '-'.join(str(n) for n in sorted_ans)
                        if key not in k:
                            k[key] = True
                            ans.append(sorted_ans)
        return ans

