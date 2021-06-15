class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        ret = set()
        dic = {}
        l = len(rooms)
        for i in range(l): dic[i] = rooms[i]
        def dfs(i):
            ret.add(i)
            if not dic[i]:
                return
            while dic[i]:
                key = dic[i].pop()
                dfs(key)
        dfs(0)
        return len(ret) == l