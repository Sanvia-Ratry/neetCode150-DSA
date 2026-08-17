class Solution:
    def isPalindrome(self, s: str) -> bool:

        sortedStr = "".join([char.lower() for char in s if char.isalnum()])

        bool = True

        for i in range(len(sortedStr)):
            
                j = len(sortedStr) - i - 1
                if sortedStr[i] != sortedStr[j]:
                    bool = False
                

        return bool
        