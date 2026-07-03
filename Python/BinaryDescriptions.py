#2196. Create Binary Tree From Descriptions

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        nodes = {}
        children = set()

        for parent_val, child_val, is_left in descriptions:
            if parent_val not in nodes :
                nodes[parent_val] = TreeNode(parent_val)
            parent_node = nodes[parent_val]

            if child_val not in nodes :
                nodes[child_val] = TreeNode(child_val)
            child_node = nodes[child_val]

            if is_left == 1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

            children.add(child_val)

        for parent_val in nodes:
            if parent_val not in children :
                return nodes[parent_val]
