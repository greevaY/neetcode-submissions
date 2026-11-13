class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     i = 0
     while i < len(nums):
        x = target - nums[i]
        y = nums.copy()
        y.pop(i)
        if x in y:
            a = y.index(x)
            return [i, (a+1)]
        i = i + 1