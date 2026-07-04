#3954. Sum of Compatible Numbers in Range I

class Solution(object):
    def sumOfGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        compatible=[]
        for x in range(max(n-k,1),n+k+1) :
            if abs(n-x)<=k and (n&x)==0 :
                compatible.append(x)

        answer=0
        for i in compatible:
            answer+=i

        return answer
