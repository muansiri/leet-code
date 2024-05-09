class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        ans = []
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def recursive(s, digits):
            if not digits:
                ans.append(s)
            else:
                for letter in phone_map[digits[0]]:
                    recursive(s + letter, digits[1:])

        recursive("", digits)
        return ans
