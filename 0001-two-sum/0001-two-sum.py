class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        MyDict = {} # value : index
        
        for indx, num in enumerate(nums):
            diff  = target - num
            if diff in MyDict:
                return [MyDict[diff], indx]
            MyDict[num] = indx
        return
        