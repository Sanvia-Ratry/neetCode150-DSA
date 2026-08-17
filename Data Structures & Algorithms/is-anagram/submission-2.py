class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = False

        if len(s) == len(t):
    
            for i in range(len(s)):
                    if s[i] in t:
                        result = True
                        t = t.replace(s[i],"",1)
                    else:
                        result = False
                        return result
        
        return result
        