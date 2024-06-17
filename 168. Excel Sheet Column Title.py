class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if not columnNumber:
            return ""
        columnNumber, remain = divmod(columnNumber - 1, 26)
        return self.convertToTitle(columnNumber) + chr(65 + remain)
