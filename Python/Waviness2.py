#3753. Total Waviness of Numbers in Range II

class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def solve(N):
            if N < 100: 
                return 0 
                
            s = str(N)
            memo = {}

            def dfs(index, tight, leading_zero, prev, curr):
                if index == len(s):
                    return (1, 0)
                
                state = (index, tight, leading_zero, prev, curr)
                if state in memo:
                    return memo[state]
                
                limit = int(s[index]) if tight else 9
                cnt, total_sum = 0, 0
                
                for digit in range(0, limit + 1):
                    next_tight = tight and (digit == limit)
                    next_leading_zero = leading_zero and (digit == 0)
                    
                    next_prev = curr
                    next_curr = -1 if next_leading_zero else digit
                    
                    sub_cnt, sub_sum = dfs(index + 1, next_tight, next_leading_zero, next_prev, next_curr)

                    if not next_leading_zero and prev != -1 and curr != -1:
                        if (prev < curr and curr > digit) or (prev > curr and curr < digit):
                            total_sum += sub_cnt
                    
                    cnt += sub_cnt
                    total_sum += sub_sum
                    
                memo[state] = (cnt, total_sum)
                return memo[state]
            return dfs(0, True, True, -1, -1)[1]
        return solve(num2) - solve(num1 - 1)
