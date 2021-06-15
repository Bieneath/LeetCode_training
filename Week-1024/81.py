# 这题和I不同，要考虑如下两种情况11101、10111以及1201111
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        le, ri = 0, len(nums) - 1
        while le <= ri:
            mid = le + ri >> 1
            if nums[mid] == target: return True
            while le < mid and nums[le] == nums[mid]:
                le += 1
            if nums[le] <= nums[mid]: # le~mid是升序；注意仅仅是le~mid升序！
                if nums[le] <= target < nums[mid]:
                    ri = mid - 1
                else: # 左侧取值范围是[nums[le], nums[mid]]，不在这个范围内必然是在右侧！
                    le = mid + 1
            else: # 右侧是升序
                if nums[mid] < target <= nums[ri]: # 因为右侧必然是升序，因此检查target是否在[nums[mid], nums[ri]]范围内
                    le = mid + 1
                else:
                    ri = mid - 1
        return False