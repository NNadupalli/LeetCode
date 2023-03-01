class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        MyDict = {}
        
        
        for num in arr:
            if num not in MyDict:
                MyDict[num] = 1
            else:
                MyDict[num]+= 1
        MySet = set(MyDict.values())
        
        return len(MySet) == len(MyDict)
                
        
        