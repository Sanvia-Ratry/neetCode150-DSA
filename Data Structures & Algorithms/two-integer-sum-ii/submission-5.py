class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

       
        i = 0
        j = len(numbers)-1

        while(i!=j):

            result = numbers[j] + numbers[i]
            if result < target:
                i += 1
            elif target< result:
                j -=1

            else:
                return [i+1, j+1]

           


        