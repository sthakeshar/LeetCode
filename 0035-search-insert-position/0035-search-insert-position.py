class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n_len=len(nums)
        if nums[0]>target:
            return 0

        if nums[n_len-1]<target:
            return n_len
            
        for i in range(n_len):
            if nums[i]==target:
                return i
                break
            elif nums[i]>target:
                return i
