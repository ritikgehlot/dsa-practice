class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones = [
            "", "One", "Two", "Three", "Four",
            "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen",
            "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"
        ]

        tens = [
            "", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        def convert(n):
            if n < 20:
                return ones[n]

            if n < 100:
                result = tens[n // 10]

                if n % 10:
                    result += " " + ones[n % 10]

                return result

            result = ones[n // 100] + " Hundred"

            if n % 100:
                result += " " + convert(n % 100)

            return result

        result = []

        if num >= 1_000_000_000:
            result.append(convert(num // 1_000_000_000))
            result.append("Billion")
            num %= 1_000_000_000

        if num >= 1_000_000:
            result.append(convert(num // 1_000_000))
            result.append("Million")
            num %= 1_000_000

        if num >= 1000:
            result.append(convert(num // 1000))
            result.append("Thousand")
            num %= 1000

        if num > 0:
            result.append(convert(num))

        return " ".join(result)