class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2

            # 1. Found it?
            if nums[mid] == target:
                return mid

            # 2. Left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:   # target is inside the left range
                    r = mid - 1                     # search left
                else:
                    l = mid + 1                     # not there, so search right

            # 3. Otherwise, the right half is sorted
            else:
                if nums[mid] < target <= nums[r]:   # target is inside the right range
                    l = mid + 1                     # search right
                else:
                    r = mid - 1                     # not there, so search left

        return -1
