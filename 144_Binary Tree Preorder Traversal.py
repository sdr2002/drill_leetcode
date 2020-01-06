# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        trav = []
        jobs = list([root])

        while jobs:    
            job = jobs.pop()

            if isinstance(job,int):
                trav.append(job)
            else:
                if not(job.right is None):
                    jobs.append(job.right)

                if not(job.left is None):
                    jobs.append(job.left)                
                jobs.append(job.val)

        return trav

    def preorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """        
        trav = []
        def preorder(node):
            if node is None:
                return
            else:
                trav.append(node.val)
                preorder(node.left)
                preorder(node.right)
               
        preorder(root)
        return trav
