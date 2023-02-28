class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        MyDict = {}
        
        for indx, num in enumerate(sorted(nums)):
            if num not in MyDict:
                MyDict[num] = indx
        
        return [MyDict[num] for num in nums]
        