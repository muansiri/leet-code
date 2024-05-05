import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cleaned_p = re.sub(r'\*{2,}', '*', p)
        matches = re.findall(f"^{cleaned_p}$", s)
        return bool(matches)
