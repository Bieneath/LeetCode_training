# 这题像是变形版的爬楼梯，这题的关键是在dp[i]如何继承前面的编码方法数。如果s[i]自身合法(s[i]在'1'~'9'之间)，表明s[i]可以作为单独一个字母并入前面的编码字符串中，此时dp[i]可以继承dp[i-1]的编码方法数。此外s[i]可以与s[i-1]合并，如果s[i-1:s+1]合法('10'~'26'之间)，表明s[i-1:i+1]可以作为单独的一个字母并入前面的编码字符串中，此时dp[i]可以继承dp[i-2]的编码方法数。
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        s = '#' + s # 小技巧，方便编程
        valid_1 = set(map(str, [_ for _ in range(1, 10)]))
        valid_2 = set(map(str, [_ for _ in range(10, 27)]))
        dp = [0] * len(s)
        dp[0] = dp[1] = 1 # s['#']对应的dp[0]默认为1，因为排除了s[1] == 0的情况，所以dp[1]一定能继承dp[0]的1。
        for i in range(2, len(s)):
            if s[i] in valid_1:
                dp[i] += dp[i-1]
            if s[i-1:i+1] in valid_2:
                dp[i] += dp[i-2]
        return dp[-1]