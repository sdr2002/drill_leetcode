import ipdb
dbg = ipdb.set_trace

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return None
        
        asc = []
        def inorder(node):
            if node is None:
                return
            else:
                if len(asc) >= k:
                    return
                else:
                    inorder(node.left)
                    asc.append(node.val)
                    if len(asc) >= k:
                        return
                    inorder(node.right)
                    return
        #dbg()
        inorder(root)
        return asc[k-1]

if __name__ == "__main__":
    s = Solution()
    tn = TreeNode(3)
    tn.left = TreeNode(1)
    tn.right = TreeNode(4)
    tn.left.right = TreeNode(2)

    print(s.kthSmallest(tn,1))
