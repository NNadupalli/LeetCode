class Solution:
    def repeatedCharacter(self, s: str) -> str:
        Mset  = set()

        for sa in s:
            if sa in Mset :
                return sa
            Mset.add(sa)
        return 

    #Time complexity = O(n)
    #Space complexity = O(1) since the string is part of english alphabet which is always 26 letters