class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        sum = ""
        aIndex = len(a) - 1
        bIndex = len(b) - 1

        while aIndex >= 0 or bIndex >= 0 or carry:
            if aIndex >= 0:
                carry += int(a[aIndex])

            if bIndex >= 0:
                carry += int(b[bIndex])

            sum = str(carry % 2) + sum
            carry //= 2

            aIndex -= 1
            bIndex -= 1

        return sum