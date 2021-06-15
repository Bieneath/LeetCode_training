# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        le, ri = 1, n
        while le <= ri:
            mid = le + (ri - le >> 1)
            ret = guess(mid)
            if ret == 0:
                return mid
            if ret == -1:
                ri = mid - 1
            elif ret == 1:
                le = mid + 1
        return