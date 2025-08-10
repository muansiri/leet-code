import re
class Solution:
    def myAtoi(self, s: str) -> int:
        pattern = r'\s*([-+]?[0-9]+).*'
        match = re.match(pattern, s)
        if match:
            result = int(match.group(1))
            if result < -2 ** 31:
                return -2 ** 31
            elif result > 2 ** 31 -1:
                return 2 ** 31 -1
            else:
                return result
        return 0
