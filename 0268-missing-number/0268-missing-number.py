class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        ans = 0
        n = len(nums)
        
        for i in range(n+1):
            if i not in nums: 
        #Time complexity of if condition above is O(n) i.e. checking if an element exists in an array is O(n) and not O(1)     
                return i

            
        return
        
        