# 参考之前写得算法，想要提高算法运算速度，要理清一个概念，并不是说递归到某个n发现n没有前置条件才return True；我们需要在“未被访问”、“已被访问”的状态上再加入一种状态“访问中”，根据题意，只有当遇到“访问中”状态，才表明该图出现的环。而遇到“已被访问”的状态，直接返回True即可。
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(set) # 该字典用于记录课程n与其所有的前置课程
        for k, v in prerequisites:
            dic[k].add(v)
        check = [0] * numCourses # 0表示未被访问，1表示已被访问(同时表示该课程能被合法选修))，-1表示访问中
        
        def dfs(n):
            if n not in dic or check[n] == 1:
                check[n] = 1
                return True
            if check[n] == -1: # 如果当前递归路过n，表示n正在被访问，此时如果再次被访问，表示图中出现了环，直接返回False
                return False
            check[n] = -1 # 递归过程中先将当前节点n标记为访问中
            for v in dic[n]: # 根据题意，只有n的所有前置条件课程全部合法，当前课程n才能被选修，所以当所有的dfs(v)都是True才返回True
                if not dfs(v):
                    return False
            check[n] = 1
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True

# from collections import defaultdict
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         dic = defaultdict(set)
#         for k, v in prerequisites:
#             dic[k].add(v)
#         check = [1] * numCourses # 图遍历，需要一个map防止走重复路线
#         def DFS(n):
#             if n not in dic:
#                 return True
#             for v in dic[n]:
#                 if check[v]:
#                     check[v] = 0
#                     if not DFS(v):
#                         return False
#                     check[v] = 1
#                 else:
#                     return False
#             return True

#         for n in range(numCourses):
#             # print('n=', n)
#             if not DFS(n):
#                 return False
#         return True

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         # 拓扑结构图第一步：构建图
#         course_map = [[] for _ in range(numCourses)]
#         courses = [0] * numCourses # 0: unvisited, -1: visiting, 1: visited
#         for it in prerequisites: 
#             course_map[it[1]].append(it[0])
        
#         # 第二步：构建一个递归格式，使得输入一个节点，能递归它的全部子孙节点
#         def DFS(i):
#             if courses[i] == -1:
#                 return False
#             if courses[i] == 1:
#                 return True
#             courses[i] = -1 # 标记i节点正在被访问
#             for j in course_map[i]:
#                 if not DFS(j):
#                     return False
#             courses[i] = 1
#             return True
        
#         # 第三步：遍历所有节点，都用第二步的递归模式去递归
#         for i in range(numCourses):
#             if not DFS(i):
#                 return False
#         return True