class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        l = len(nums)
        for num in nums:
            if num == val:
                l-=1
        m = l
        for i in range(len(nums)):
            if(nums[i] == val):
                for j in range(i+1, len(nums)):
                    if nums[j] != val:
                        nums[i] = nums[j]
                        nums[j] = val
                        break


        return l


            
        