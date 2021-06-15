# 自己得出的经验就是假设[le, ri]满足条件，则能得到的子串数目为n=len(s)-ri，因为可以逐个在[le, ri]的基础上往右追加字符，都能满足条件。然后再考虑左侧边界，不停的往右移动左侧边界m次，直到不满足条件为止，那么当前能获得新的满足条件的字符串个数为m*n。
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dic = {c:0 for c in 'abc'} # 这种建立字典的方法比较巧妙
        le = ret = 0
        for ri, v in enumerate(s):
            dic[v] += 1
            pre = le
            while 0 not in dic.values(): # 当[le, ri]符合条件时，尝试右移左边界
                dic[s[le]] -= 1
                le += 1
            ret += (le - pre) * (len(s) - ri) # 右边的乘数n=len(s)-ri是固定的，m为左边界移动次数
        return ret