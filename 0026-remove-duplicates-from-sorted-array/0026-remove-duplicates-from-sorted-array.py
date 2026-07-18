class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # 'k' is the pointer for the position of the last unique element
        k = 0 
        
        # Start from the second element (index 1)
        for i in range(1, len(nums)):
            # If we find a new unique number
            if nums[i] != nums[k]:
                k += 1           # Move the unique pointer forward
                nums[k] = nums[i] # Update the position with the new value
        
        # The number of unique elements is k + 1
        return k + 1