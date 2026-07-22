class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
    
    # Loop until both strings are fully processed and no carry is left
        while i >= 0 or j >= 0 or carry > 0:
            sum_val = carry
        
        # Add digit from string 'a' if available
            if i >= 0:
                sum_val += int(a[i])
                i -= 1
            
        # Add digit from string 'b' if available
            if j >= 0:
                sum_val += int(b[j])
                j -= 1
            
        # The new digit to record is the remainder (sum_val % 2)
            result.append(str(sum_val % 2))
        
        # The new carry is how many times 2 fits into sum_val (sum_val // 2)
            carry = sum_val // 2
        
    # Since we added digits from right to left, the result is backwards.
    # We reverse it to get the final binary string.
        return "".join(reversed(result))