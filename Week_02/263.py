class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0: return False
        for divid in [5, 3, 2]:
            while num % divid is 0:
                num //= divid
        return 1 == num