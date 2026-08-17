class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mysortedDict = defaultdict(list)

        for i in range(len(strs)):

            key = "".join(sorted(strs[i]))
            mysortedDict[key].append(strs[i])

        return list(mysortedDict.values())









        
        