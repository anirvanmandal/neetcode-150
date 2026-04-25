class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if hashMap.get(num) == None:
                hashMap[num] = 0
            hashMap[num] += 1
        buckets = [[] for _ in range(len(nums))]
        
        for key, value in hashMap.items():
            buckets[value - 1].append(key)

        array_list = []
        i = 0;
        for ints in buckets[::-1]:
            for integer in ints:
                array_list.append(integer)
                i += 1
                if i == k:
                    break
            if i == k:
                break

        return array_list
