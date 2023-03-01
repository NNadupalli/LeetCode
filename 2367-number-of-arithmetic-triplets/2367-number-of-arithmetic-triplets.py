class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        result = []
        
        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if ((nums[j]- nums[i] == diff) and (nums[k]- nums[j] == diff)):
                        result.append((i,j,k))
        
        return len(result)
        