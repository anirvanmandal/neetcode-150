class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}

        for char in s:
            if hashS.get(char) is None:
                hashS[char] = 0
            hashS[char] += 1
        
        for char in t:
            if hashT.get(char) is None:
                hashT[char] = 0
            hashT[char] += 1

        return hashS == hashT
        