class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        
        prev = 1
        current = 1
        
        for _ in range(2, n + 1):
            temp = current
            current = prev + current
            prev = temp
            
        return current