#2011. Final Value of Variable After Performing Operations

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        return sum(1 if "+" in i  else -1 for i in operations)
