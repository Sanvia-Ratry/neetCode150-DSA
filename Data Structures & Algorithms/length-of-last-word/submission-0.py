class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        newString = s.split()
        return len(newString[len(newString)-1])