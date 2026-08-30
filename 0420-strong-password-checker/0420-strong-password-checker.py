class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        lower = 0
        upper = 0
        digit = 0

        for ch in password:
            if ch.islower():
                lower = 1
            elif ch.isupper():
                upper = 1
            elif ch.isdigit():
                digit = 1

        missing = 3 - (lower + upper + digit)

        if n < 6:
            return max(missing, 6 - n)

        replace = 0
        one = 0
        two = 0

        i = 0

        while i < n:
            j = i

            while j < n and password[j] == password[i]:
                j += 1

            length = j - i

            if length >= 3:
                replace += length // 3

                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1

            i = j

        if n <= 20:
            return max(missing, replace)

        delete = n - 20

        use = min(delete, one)
        replace -= use
        delete -= use

        use = min(delete, two * 2)
        replace -= use // 2
        delete -= use

        replace -= delete // 3

        return (n - 20) + max(missing, replace)