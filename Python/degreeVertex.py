#3898. Find the Degree of Each Vertex

class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(matrix)):
            degree=0
            for j in range(len(matrix)):
                if matrix[i][j]==1:
                    degree+=1
            ans.append(degree)

        return ans
