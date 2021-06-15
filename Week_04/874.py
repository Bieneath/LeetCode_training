class Solution:
    def robotSim(self, commands: List[int], obs: List[List[int]]) -> int:
        max_val = 0
        obs = set(map(tuple, [_ for _ in obs])) # 将obs转换为set类型，方便查询
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        cur_d = 0
        x, y = 0, 0 # x为横向坐标值，y为纵向坐标值
        for cmd in commands:
            if -1 == cmd:
                cur_d = (cur_d + 1) % 4
            elif -2 == cmd:
                cur_d = (cur_d - 1) % 4
            else:
                while cmd:
                    cmd -= 1
                    next_x = x + directions[cur_d][0]
                    next_y = y + directions[cur_d][1]
                    if (next_x, next_y) in obs: # 如果撞上障碍物，余下的步数不用执行直接break
                        break
                    x, y = next_x, next_y
            max_val = max(max_val, x**2+y**2)
        return max_val