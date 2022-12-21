import re

class Solution(object):
    def myAtoi(self, s):
        try:
            capture = re.findall('(^[\+\-\0]*\d+)', s.strip())
            result = int(capture[0]) if len(capture) else 0
            if result < -2 ** 31:
                return -2 ** 31
            elif result > 2 ** 31 - 1:
                return 2 ** 31 - 1
            return result
        except:
            return 0
        """
        :type s: str
        :rtype: int
        """