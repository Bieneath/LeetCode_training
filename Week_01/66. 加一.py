class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(-1, -len(digits)-1, -1):
            t = digits[i] + carry
            digits[i], carry = t%10, t//10
        if carry:
            digits = digits[::-1]
            digits.append(carry)
            digits = digits[::-1]
        return digits