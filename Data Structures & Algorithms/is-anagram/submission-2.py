class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = defaultdict(int)
        hashT = defaultdict(int)

        if len(s) != len(t):
            return False

        for char in s:
            hashS[char] += 1
        
        for char in t:
            hashT[char] += 1

        return hashS == hashT
        