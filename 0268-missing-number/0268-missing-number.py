class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        ans = 0
        n = len(nums)
        
        for i in range(n+1):
            if i not in nums:
                return i

            
        return
        
        