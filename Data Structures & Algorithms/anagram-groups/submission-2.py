class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for index, string in enumerate(strs):
            charsArray = [0] * 26
            for char in string:
                charsArray[ord(char) - 97] += 1
            strArray = ','.join([str(i) for i in charsArray])
            if hashMap.get(strArray) == None:
                hashMap[strArray] = []
            hashMap[strArray].append(string)
        
        return list(hashMap.values())
