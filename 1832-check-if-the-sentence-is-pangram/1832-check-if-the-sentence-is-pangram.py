class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        if len(sentence)<26:
            return False
        
        mset = set()
        
        for letter in sentence:
            if letter not in mset:
                mset.add(letter)
                
        return len(mset) >=26
        