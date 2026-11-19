class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        
        counts = defaultdict(int)
        
        if len(nums)>1:
            for num in nums:
                    counts[num] +=1
            return max(counts, key = counts.get)
        else:
            return nums[0]
        
        
        
