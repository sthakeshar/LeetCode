class Solution(object):
    def strStr(self, haystack, needle):
        h_len = len(haystack)
        n_len = len(needle)
        
        # If the needle is empty, it's usually defined to be at index 0
        if n_len == 0:
            return 0
        
        # We only need to loop until the remaining haystack is at least 
        # as long as the needle
        for i in range(h_len - n_len + 1):
            # Check if all characters match starting at position i
            match = True
            for j in range(n_len):
                if haystack[i + j] != needle[j]:
                    match = False
                    break  # Stop checking this window as soon as one char fails
            
            # If the inner loop finished without setting match to False
            if match:
                return i
                
        return -1