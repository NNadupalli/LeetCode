class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        arr.sort()
        count = 0
        run_length = 1
        
        for i in range(len(arr)):
            if arr[i-1]!= arr[i]:
                if arr[i-1]+1 == arr[i]:
                    count += run_length
                run_length = 0
            run_length += 1
        
        return count
        
        
#Time complexity : O(nlogn)
#Space complexity: O(n) to O(1) depending on the type of sort algorithm used to implement array sort in python
        