class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        MysDict = {}
        MytDict = {}
        
        for i in range(len(s)):
            MysDict[s[i]] = MysDict.get(s[i],0)+1
            MytDict[t[i]] = MytDict.get(t[i],0)+1
                
                      

        return MysDict == MytDict
        
            
        