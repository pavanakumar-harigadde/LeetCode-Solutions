#3190. Find Minimum Operations to Make All Elements Divisible by Three

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if i%3 != 0:
                count+=1
        return count
