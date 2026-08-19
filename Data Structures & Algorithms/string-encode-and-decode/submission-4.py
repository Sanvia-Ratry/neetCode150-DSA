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

                if s[i].isdigit():
                    num_str = ""
                    while(i<len(s) and s[i].isdigit()):
                        num_str += s[i]
                        i += 1
                    count = int(num_str)
                    if s[i] == "*" and (i+count+1)<len(s) and s[i+count+1] == "*":
                        myList.append(s[i+1:count+i+1])
                        i += count+1
                else:
                    i += 1
            return myList