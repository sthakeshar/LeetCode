class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        y=x
        rev=0
        while x != 0:
            temp=x%10
            rev=rev*10+temp
            x=x/10
        return rev==y