class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        higher = len(nums) - 1
        return self.searchRec(nums, target, lower, higher)
    
    def searchRec(self, nums: List[int], target: int, lower: int, higher: int) -> int:
        if lower > higher:
            return -1

        mid = (lower + higher) // 2

        if nums[mid] > target:
            return self.searchRec(nums, target, lower, mid - 1)

        elif nums[mid] < target:
            return self.searchRec(nums, target, mid + 1, higher)

        else:
            return mid