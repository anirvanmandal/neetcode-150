class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {};
        for index, num in enumerate(nums):
            if hash.get(num) is not None:
                return True
            hash[num] = index
        return False

        