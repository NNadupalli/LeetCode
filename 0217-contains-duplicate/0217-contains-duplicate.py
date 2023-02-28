class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        MyDict = {}
        
        for num in nums:
            if num in MyDict:
                return True
            else:
                MyDict[num] = 1
        return
        