class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        my_dict = defaultdict(int)
        for index,value in enumerate(numbers, start=1):

            my_dict[value] = index
        i = 0
        j = i+1
        while(i<j):

            result = target - numbers[i]

            if result in my_dict:
                return [i+1,my_dict[result]]


            i += 1
            j = i+1


        