#3731. Find Missing Elements

class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        maximum = max(nums)
        minimum = min(nums)
        result = []
        for i in range (minimum, maximum):
            if i not in nums:
                result.append(i)
        return result
