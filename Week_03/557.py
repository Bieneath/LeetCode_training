'''
class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s[::-1].split()
        ret = ''
        for x in temp[::-1]:
            ret += ' ' + x
        return ret[1:]
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(x[::-1] for x in s.split())