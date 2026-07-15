class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        sortedStrs=sorted(strs)
        Longest_Common_prefix=''
        first=sortedStrs[0]
        last=sortedStrs[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return Longest_Common_prefix
            Longest_Common_prefix+=first[i]
        return Longest_Common_prefix