#2574. Left and Right Sum Differences

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0]*n
        rightSum = [0]*n
        answer = [0]* n

        for i in range(len(nums)):
            leftSum[0] = 0

            rightSum[len(nums)-1]=0
            left = 0
            right = 0

            for j in range(i) :
                left += nums[j]
            leftSum[i] = left

            for j in range(i+1, len(nums)):
                right += nums[j]
            rightSum[i] = right

            answer[i] = abs(leftSum[i] - rightSum[i])
        return answer
