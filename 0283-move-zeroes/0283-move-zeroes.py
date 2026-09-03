class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert = 0

        for i, num in enumerate(nums):
            if num:
                nums[insert], nums[i] = nums[i], nums[insert]
                insert += 1