class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        count = len(s)
        if count == 0:
            return True
        i = 0
        j = 0
        while(j<len(s) and i<len(t)):

            if t[i] == s[j]:
                j +=1
                i +=1
                count -=1
            else:
                i +=1

            if count == 0:
                return True
        return False
