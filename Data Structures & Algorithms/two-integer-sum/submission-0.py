class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {};
        for i, num in enumerate(nums):
            if hash.get(target - num) is not None:
                return [hash[target - num], i]
            else:
                hash[num] = i