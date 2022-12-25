class Solution(object):
    def intToRoman(self, num):
        a = ''
        while num > 0:
            if num >= 1000:
                a += 'M' * (num // 1000)
                num %= 1000
            elif num >= 900:
                a += 'CM' * (num // 900)
                num %= 900
            elif num >= 500:
                a += 'D' * (num // 500)
                num %= 500
            elif num >= 400:
                a += 'CD' * (num // 400)
                num %= 400
            elif num >= 100:
                a += 'C' * (num // 100)
                num %= 100
            elif num >= 90:
                a += 'XC' * (num // 90)
                num %= 90
            elif num >= 50:
                a += 'L' * (num // 50)
                num %= 50
            elif num >= 40:
                a += 'XL' * (num // 40)
                num %= 40
            elif num >= 10:
                a += 'X' * (num // 10)
                num %= 10
            elif num >= 9:
                a += 'IX' * (num // 9)
                num %= 9
            elif num >= 5:
                a += 'V' * (num // 5)
                num %= 5
            elif num >= 4:
                a += 'IV' * (num // 4)
                num %= 4
            elif num >= 1:
                a += 'I' * (num // 1)
                num %= 1
        return a
        """
        :type num: int
        :rtype: str
        """