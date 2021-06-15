class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        for i in range(len(nums)):
            while zero < len(nums) and nums[zero]:
                zero += 1
            if nums[i] and zero < i:
                nums[zero], nums[i] = nums[i], nums[zero]

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         explorer = zero_pos = 0
#         for explorer in range(len(nums)):
#             if nums[explorer] != 0:
#                 nums[explorer], nums[zero_pos] = nums[zero_pos], nums[explorer]
#             if nums[zero_pos] != 0:
#                 zero_pos += 1

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         if not nums: return None
#         zero = 0
#         for i in range(len(nums)):
#             if not nums[i]: continue
#             while zero < len(nums) and nums[zero]: 
#                 zero += 1
#                 continue
#             if zero < i:
#                 nums[zero], nums[i] = nums[i], nums[zero]
#         return nums