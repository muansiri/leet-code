class Solution:
    def intToRoman(self, num: int) -> str:
        romans = [
            { 'symbol': 'M', 'value': 1000 },
            { 'symbol': 'CM', 'value': 900 },
            { 'symbol': 'D', 'value': 500 },
            { 'symbol': 'CD', 'value': 400 },
            { 'symbol': 'C', 'value': 100 },
            { 'symbol': 'XC', 'value': 90 },
            { 'symbol': 'L', 'value': 50 },
            { 'symbol': 'XL', 'value': 40 },
            { 'symbol': 'X', 'value': 10 },
            { 'symbol': 'IX', 'value': 9 },
            { 'symbol': 'V', 'value': 5 },
            { 'symbol': 'IV', 'value': 4 },
            { 'symbol': 'I', 'value': 1 },
        ]
        result, i = "", 0
        while num > 0:
            if num >= romans[i]["value"]:
                result += romans[i]["symbol"]
                num -= romans[i]["value"]
            else:
                i += 1
        return result
