class Solution:
    def numberToWords(self, num: int) -> str:
        dict = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
                9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
                16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
                50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 100: 'Hundred', 1000: 'Thousand',
                1_000_000: 'Million', 1_000_000_000: 'Billion'}
        if num == 0:
            return "Zero"

        def helper(num: int):
            # 注意顺序，是有细节的
            res = []
            if 100 <= num < 1000:
                res.append(dict[num//100])
                res.append(dict[100])
                num -= (num // 100) * 100
            if 0 < num <= 20:
                res.append(dict[num])
            elif num > 0:
                res.append(dict[(num // 10) * 10])
                res.append(dict[num % 10]) if num % 10 != 0 else None
            return res

        carrier = [1_000_000_000, 1_000_000, 1000, 1]
        res = []
        for c in carrier:
            if num / c < 1000 and num // c > 0:
                res += helper(num // c)
                if c != 1:
                    res.append(dict[c])
                num -= (num // c) * c
        return " ".join(res)


# print(Solution().numberToWords(123))
# print(Solution().numberToWords(12345))
# print(Solution().numberToWords(1234567))
print(Solution().numberToWords(100))