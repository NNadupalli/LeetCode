class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        all_word = set(word1 + word2)
        
        for word in all_word:
            if abs(word1.count(word) - word2.count(word)) >=4:
                return False
        
        return True
                
                
        
        