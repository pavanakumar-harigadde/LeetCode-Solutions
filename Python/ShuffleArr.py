#1470. Shuffle the Array

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)//2
        arr = []
        for i in range(n):
            arr.append(nums[i])
            arr.append(nums[i+n])
        return arr
