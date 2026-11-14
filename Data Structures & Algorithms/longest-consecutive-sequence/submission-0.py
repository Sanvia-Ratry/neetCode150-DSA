class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        current = 1;
        maxLength = 0;

        nums.sort()
        if not nums:
            return 0
        for i in range(len(nums)-1):

            if nums[i] + 1 == nums[i+1]:
                current += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                maxLength = max(current,maxLength)
                current = 1

        return max(maxLength,current)


        