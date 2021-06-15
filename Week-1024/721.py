# 并查集算法
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dic = {}
        email2name = {}
        def find(x):
            if x != dic.setdefault(x, x):
                dic[x] = find(dic[x])
            return dic[x]
        for it in accounts:
            email2name[it[1]] = it[0] # 记录一下第一个邮件地址对应的用户名
            root = find(it[1]) # find(it[1])这步不能少，因为有可能出现没有it[2]的情况
            for mail in it[2:]:
                dic[find(mail)] = root # 将所有的邮件地址归并到第一个邮件地址上
        # 返回处理
        ret = defaultdict(list)
        for key in dic: # 这点我之前不是很熟悉，可以通过遍历dic的方法查看所有在并查集中注册的元素！
            ret[find(key)].append(key) # 这里不能写成ret[dic[key]]，因为find()的过程也是更新dic字典的过程
        return [[email2name[k]] + sorted(v) for k, v in ret.items()]

# # DFS算法
# from collections import defaultdict
# class Solution:
#     def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
#         # 先构建网站之间的关系图
#         dic = defaultdict(set)
#         for it in accounts:
#             for i in range(1, len(it)):
#                 dic[it[i]] |= set(it[1:i] + it[i+1:])
#         # DFS算法，目标是通过DFS以及关系图dic将与mail相关联的所有网站都汇总起来
#         seen = set()
#         def dfs(mail):
#             if mail in seen:
#                 return set()
#             ret = {mail}
#             seen.add(mail)
#             for t in dic[mail]:
#                 ret |= dfs(t)
#             return ret
#         # 主函数部分
#         ret = []
#         for it in accounts:
#             if it[1] not in seen:
#                 ret.append([it[0]] + sorted(dfs(it[1])))
#         return ret