class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = int("".join([f'{digit}' for digit in digits]))  + 1
        return [int(char) for char in f'{digits}']
