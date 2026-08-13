#3668. Restore Finishing Order

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        arr=[]
        for i in order:
            if i in friends:
                arr.append(i)

        return arr
