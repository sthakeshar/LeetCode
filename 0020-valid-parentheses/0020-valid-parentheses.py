class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        checkMap = {'(': ')', '{': '}', '[': ']'}
        stack = []
    
        for char in s:
            # If the char is an opening bracket, add to stack
            if char in checkMap:
                stack.append(char)
            else:
                # If it's a closing bracket:
                # 1. Check if stack is not empty
                # 2. Check if the closing bracket matches the last opened one
                if stack and checkMap[stack[-1]] == char:
                    stack.pop()
                else:
                    return False 
        return not stack
