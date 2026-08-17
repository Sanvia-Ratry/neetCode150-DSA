class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        count = 0
        oldcount = 0
        while(i<len(nums)):

            if nums[i] == 1:
                count += 1
            else:
                if not oldcount:
                    oldcount = count
                    count = 0
                else:
                    if oldcount>count:
                        count = 0
                    else:
                        oldcount = count
                        count = 0
            i += 1

        if oldcount>count:
            return oldcount
        else:
            return count

