#3691.Maximum Total Subarray Value II
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n==0 or k==0:
            return 0

        K = int(math.log2(n)) +1
        st_max = [[0]*K for _ in range(n)]
        st_min = [[0]*K for _ in range(n)]

        for i in range(n):
            st_max[i][0] = nums[i]
            st_min[i][0] = nums[i]

        for j in range(1,K):
            for i in range(n-(1<<j)+1):
                st_max[i][j] = max(st_max[i][j-1], st_max[i+(1<<(j-1))][j-1])
                st_min[i][j] = min(st_min[i][j-1], st_min[i+(1<<(j-1))][j-1])

        def get_val(L:int, R:int):
            length = R-L +1
            j=int(math.log2(length))
            mx=max(st_max[L][j], st_max[R-(1<<j)+1][j])
            mn=min(st_min[L][j], st_min[R-(1<<j)+1][j])
            return mx-mn

        heap=[]
        for L in range(n):
            val=get_val(L,n-1)
            heapq.heappush(heap,(-val,L,n-1))

        total_max_value = 0
        for _ in range(k):
            neg_val, L, R = heapq.heappop(heap)
            total_max_value += (-neg_val)

            if R>L:
                next_val = get_val(L,R-1)
                heapq.heappush(heap,(-next_val, L, R-1))
        
        return total_max_value
