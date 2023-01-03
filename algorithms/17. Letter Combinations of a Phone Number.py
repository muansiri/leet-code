class Solution(object):
    map = {
        "0": "",
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letterCombine(self, a, s, digits):
        if len(s) == len(digits):
            a.append(s)
            return

        for c in self.map[digits[len(s)]]:
            self.letterCombine(a, s + c, digits)

    def letterCombinations(self, digits):
        a = []
        if digits:
            self.letterCombine(a, "", digits)
        return a
        """
        :type digits: str
        :rtype: List[str]
        """