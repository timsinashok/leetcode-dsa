"""
Idea: hashmap

Solution: 
1. use dict, store the difference of target and the current num in dict
and then keep on looping and see if hte current number which is complimentary to to the another diffrerence to make the target is in list or not
if the num is in the dict then we have already seen the complimentary number
so just return the current index and hte index of hte num which has required difference

so we have to store the difference and the index in the dict
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        diff = 0
        for i, num in enumerate(nums):
            diff = target - num
            if num in diff_dict:
                return [diff_dict.get(num), i]
            else:
                diff_dict.update({diff:i})