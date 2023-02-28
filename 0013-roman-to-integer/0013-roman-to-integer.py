class Solution:
    def romanToInt(self, s: str) -> int:
        Mydict = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        val = 0
        prev = s[0]

        for achar in s:
            if(Mydict[prev] < Mydict[achar]):
                val = val + (Mydict[achar] - Mydict[prev]) - Mydict[prev]
            else:
                val = val + Mydict[achar]
            prev = achar
        
        return val


