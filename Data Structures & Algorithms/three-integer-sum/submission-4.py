class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sList = sorted(nums)
        myset = set()
        for i in range(len(nums)):

            j = len(nums) -1
            k = i+1
            while(i<j and j > k):
                result = sList[i] + sList[k] + sList[j]
                triplet = (sList[i],sList[k],sList[j])
                if result == 0:
                    myset.add(triplet)
                    k += 1
                    j -=1
                    
                elif result < 0:
                    k +=1
                else:
                    j -=1

        return [list(t) for t in myset]


        



