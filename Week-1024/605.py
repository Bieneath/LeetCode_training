# 遍历bed，如果bed[i-1]、bed[i]、bed[i+1]都是0，则插入花。设计了一个技巧，在开头和接为分别加上[1, 0]和[0, 1]
class Solution:
    def canPlaceFlowers(self, bed: List[int], n: int) -> bool:
        bed = [1, 0] + bed + [0, 1]
        for i in range(2, len(bed) - 2):
            if bed[i-1] | bed[i] | bed[i+1] == 0:
                bed[i] = 1
                n -= 1
        return n <= 0