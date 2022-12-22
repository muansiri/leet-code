import re
class Solution(object):
    def isMatch(self, s, p):
        return True if re.match('^{}$'.format(p), s) else False

        """
        :type s: str
        :type p: str
        :rtype: bool
        """