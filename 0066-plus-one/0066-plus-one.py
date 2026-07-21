class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #(Convert list -> Number :: -> Addition +1 :: -> Number -> List
        n=0
        for i in digits:
            n=(n*10)+i
        n=n+1
        digits=[]
        while n>0:
            digits.insert(0,n%10)
            n//=10
        return digits