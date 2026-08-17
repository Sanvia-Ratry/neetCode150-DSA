class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        my_list = defaultdict(int)
        count_list = []
        for i in range(len(nums)):

            my_list[nums[i]] += 1


        for j in range(k):

            highest_count = max(my_list, key= my_list.get)
            count_list.append(highest_count)
            del my_list[highest_count]
                

        return count_list
