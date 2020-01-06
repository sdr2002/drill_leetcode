import ipdb
dbg = ipdb.set_trace

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root is None:
            return []

        jobs = [root] # stack
        trav = []

        while jobs:
            job = jobs.pop(-1)
            if isinstance(job,int):
                trav.append(job)
            else:
                if not(job.right is None):
                    jobs.append(job.right)
                jobs.append(job.val)
                if not(job.left is None):
                    jobs.append(job.left)

        return trav
            
        

    def inorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        trav = []
        def inorder(node):
            if node is None:
                return
            else:
                inorder(node.left)
                trav.append(node.val)
                inorder(node.right)
                return
        inorder(root)
        return trav

if __name__ == "__main__":
    s = Solution()
    tn = TreeNode(1)
    tn.right = TreeNode(2)
    tn.right.left = TreeNode(3)
    print(s.inorderTraversal(tn))
