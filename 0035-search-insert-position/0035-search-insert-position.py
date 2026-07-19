class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            # If we find the target, or the first number GREATER than target
            if nums[i] >= target:
                return i
        
        # If we finish the loop, it means target is larger than everything
        return len(nums)