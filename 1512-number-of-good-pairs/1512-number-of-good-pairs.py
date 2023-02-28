class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        Mydict = {} # value : index
        count_pairs = 0

        for indx, num in enumerate(nums):
            if num in Mydict:
                count_pairs += Mydict[num]
                Mydict[num]+= 1
            else:
                Mydict[num] = 1
        
        return count_pairs
            
            