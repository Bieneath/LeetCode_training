class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st, ts = {}, {}
        for i in range(len(s)):
            if s[i] not in st and t[i] not in ts:
                st[s[i]] = t[i]
                ts[t[i]] = s[i]
            elif s[i] in st and t[i] in ts and st[s[i]] == t[i] and ts[t[i]] == s[i]:
                continue
            else:
                return False
        return True