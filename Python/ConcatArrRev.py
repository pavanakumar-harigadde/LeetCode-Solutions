#3925. Concatenate Array With Reverse

class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(nums)):
            ans.append(nums[len(nums)-i-1])
        return nums+ans
