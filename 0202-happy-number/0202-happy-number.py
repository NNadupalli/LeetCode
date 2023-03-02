class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        total = 0
        visited = set()
        
        while(n!=1):
            n = str(n)
            total = 0
            
            for achar in n:
                total = total + int(achar)**2
            
            if total in visited:
                return False
            visited.add(total)
            n = total
        
        return True
        
        