#improved Solution with one while loop:
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in range(len(strs)):

            L = len(strs[i])
            newStr = str(L)+ "*" +strs[i]
            encoded_string += newStr+"*"
        return encoded_string
 
    def decode(self, s: str) -> List[str]:
        
            i = 0
            myList = []
            while (i < len(s)):

                first_delimeter = s.find("*",i)
                num_str = s[i:first_delimeter]
                count = int(num_str)
                myList.append(s[first_delimeter+1:count+first_delimeter+1])
                i = first_delimeter + 2 + count 
              
            return myList