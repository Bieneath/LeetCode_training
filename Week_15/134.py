# 一次遍历法
# 这里有个逻辑思路从i点出发，最远能到的点假设是j，如果i!=j，那么说明在gas[i]>=cost[j]，点i就是一个正反馈点，连续子串带上点i能走的更远。因此如果从i出发最远只能到j，那么(i, j]点可能都到不了j(因为死在j点上，j肯定是负反馈)。我们可以直接跳到j+1重新开始探索。此外基于多多益善的原则，如果i后面的点能顺利绕一圈，那么从i点出发肯定也能绕一圈，但是题目说明只有一种路径，所以i就是需要的点。
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 先根据gas和cost从全局判断一下时候可能顺利跑完一圈
        if sum(cost) > sum(gas): return -1
        start = remain = 0
        for i in range(len(gas)):
            remain += gas[i] - cost[i]
            if remain < 0:
                start = i + 1
                remain = 0
        return start

# # 几乎算是暴力的解法
# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         l = len(gas)
#         seq = [(gas[i]-cost[i], i) for i in range(l)]
#         seq.sort(reverse=True)
#         max_diff = seq[0][0]
#         def check(start): # 判断否能到达终点
#             remain = 0
#             for i in range(l + 1):
#                 idx = (start + i) % l
#                 remain += gas[idx] - cost[idx]
#                 if remain < 0:
#                     return False
#             return True
        
#         for diff, i in seq:
#             if diff < 0: break
#             if check(i): return i
#         return -1