class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        solution = [0,0]
        i = 0
        while(i < len(nums)-1):
            j = i+1
            while(j<len(nums)):
                if (nums[i] + nums[j] == target):
                    solution[0] = i
                    solution[1] = j
                    break
                    break
                else:
                    j = j + 1
            i = i+1
        return solution
