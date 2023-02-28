class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        MysDict = {}
        MytDict = {}
        
        for achar in s:
            if achar in MysDict :
                MysDict[achar] += 1
            else:
                MysDict[achar] =1
                
        for achar in t:
            if achar in MytDict :
                MytDict[achar] += 1
            else:
                MytDict[achar] =1
                
        if MysDict == MytDict:
            return True
        else:
            return False
        
        
            
        