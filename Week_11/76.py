# 参看 https://leetcode-cn.com/problems/minimum-window-substring/solution/tong-su-qie-xiang-xi-de-miao-shu-hua-dong-chuang-k/ 的解释。
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic, missing = Counter(t), len(t)
        i = 0
        le = ri = -1
        for j, c in enumerate(s):
            missing -= dic[c] > 0 # 只有c是t中的数字（dic[c] > 0），missing才减1
            dic[c] -= 1
            if 0 == missing:
                while dic[s[i]] < 0:
                    dic[s[i]] += 1
                    i += 1
                if -1 == ri or j - i < ri - le:
                    le, ri = i, j
                # 推动循环继续下去，主动让s[i]划出窗口，使得当前滑动窗口缺少s[i]这个元素。
                dic[s[i]] += 1
                missing += 1
                i += 1
        return '' if -1 == ri else s[le:ri+1]