class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        ans = 0
        n = len(nums)
        nums = set(nums)
        
        for i in range(n+1):
            if i not in nums: 
        #Time complexity of if condition above is O(1) i.e.
        # since nums is converted to a set, the time to check the existence of an element in a set is O(1)
                return i

            
        return
        
        