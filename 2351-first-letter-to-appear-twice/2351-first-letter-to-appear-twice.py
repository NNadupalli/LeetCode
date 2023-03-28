class Solution:
    def repeatedCharacter(self, s: str) -> str:
        Mset  = set()

        for sa in s:
            if sa in Mset :
                return sa
            else:
                Mset.add(sa)
        return 
