class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
    
        for i in range(len(strs[0])):

            char = strs[0][i]
            for s in strs[1:]:
                if len(s) == 0:
                    return ""
                if i == len(s) or char != s[i]:
                    return s[:i]
                
        return strs[0]
