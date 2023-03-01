class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        if len(sentence)<26:
            return False
        
        MyDict = {}
        
        for letter in sentence:
            if letter not in MyDict:
                MyDict[letter] = 1
                
        return len(MyDict.keys()) >=26
        