class Solution:
    def repeatedCharacter(self, s: str) -> str:
        Mydict = {}

        for sa in s:
            if sa in Mydict :
                Mydict[sa] += 1
                if Mydict[sa] ==2:
                    return sa
            else:
                Mydict[sa] = 1
        return 
