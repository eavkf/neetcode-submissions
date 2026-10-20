class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)
        if sorted(list(numsSet)) == sorted(nums):
            return False
        return True