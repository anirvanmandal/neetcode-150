class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}

        for char in s:
            val = hashS.get(char, 0)
            hashS[char] = val + 1
        
        for char in t:
            val = hashT.get(char, 0)
            hashT[char] = val + 1

        return hashS == hashT
        