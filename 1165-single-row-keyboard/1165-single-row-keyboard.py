class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        MyDict = {}
        Time = 0
        init_time = 0
        
        for indx, key in enumerate(list(keyboard)):
            MyDict[key] = indx
            
        for achar in word:
            Time = Time + abs(init_time - MyDict[achar])
            init_time = MyDict[achar]
            
        return Time
        