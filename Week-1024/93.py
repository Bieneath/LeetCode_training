# 递归+回溯解法
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        valid_nums = set(map(str, range(256)))
        ret = []
        def get_ip(start, count, path):
            if not count:
                if start == len(s):
                    ret.append(path.lstrip('.'))
                return
            for i in range(1, 4): # 切片和range组合的时候最后一位要多预留2！！！
                if s[start:start+i] in valid_nums:
                    get_ip(start+i, count-1, path + '.' + s[start:start+i])
        get_ip(0, 4, "")
        return ret