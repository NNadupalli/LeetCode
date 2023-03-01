class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        MyDict = {}
        i = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        res = ""
        MyDict [' '] = ' '
        
        for letter in key:
            if letter not in MyDict:
                MyDict[letter] = alphabet[i]
                i+= 1
        
        for letter in message:
            res = res + MyDict[letter]
            
        return res
        