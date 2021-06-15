class Solution:
    def getPermutation(self, nums: int, k: int) -> str:
        factorial_table = [1] # 从0到n的阶乘结果表
        for l in range(1, nums):
            factorial_table.append(factorial_table[-1]*l)
        k = k - 1 # 求第k个实际上在计算机中就是求第k-1个
        nums = [_ for _ in range(1, nums+1)]
        ret = ''
        while nums:
            fa = factorial_table[len(nums)-1] # 求出len(nums) - 1的阶乘fa
            ret += str(nums.pop(k // fa)) # 将下标为k//fa的nums中的元素添加到字符串上
            k = k % fa # k为减去x个fa后的余数
        return ret