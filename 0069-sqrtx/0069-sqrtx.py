class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        
        left = 1
        right = x // 2
        ans = 0
    
        while left <= right:
            mid = (left + right) // 2
            
            # If mid squared is exactly x, we found it
            if mid * mid == x:
                return mid
            # If mid squared is less than x, try a larger number
            elif mid * mid < x:
                ans = mid  # Keep track of it as a potential answer
                left = mid + 1
            # If mid squared is too large, try a smaller number
            else:
                right = mid - 1
                
        return ans