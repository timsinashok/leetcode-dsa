class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = []
        j = 0
        for i in range(len(nums)):
            if (nums[i] not in unique):
                unique.append(nums[i])
                nums[j] = nums[i]
                j += 1
        print(nums)
        return len(unique)