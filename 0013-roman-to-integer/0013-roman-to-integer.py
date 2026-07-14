class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanMap={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        n = len(s)
        
        for i in range(n):
            cur = romanMap[s[i]]
            
            # Check if there is a next character and compare
            if i + 1 < n and cur < romanMap[s[i + 1]]:
                result -= cur
            else:
                result += cur
                
        return result  
        