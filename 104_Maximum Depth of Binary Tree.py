class Solution(object):
    def maxDepth(self,root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if (root is None):
            return 0;
        else:
            return self.getDepth(root);
    def getDepth(self,node):
        chd_left = node.left;
        chd_right = node.right;
        
        if (chd_left is None) and (chd_right is None):
            return 1;
        elif not(chd_left is None) and (chd_right is None):
            return self.getDepth(chd_left)+1;
        elif (chd_left is None) and not(chd_right is None):
            return self.getDepth(chd_right)+1;
        else:
            return max(self.getDepth(chd_left)+1,self.getDepth(chd_right)+1);

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

if __name__ == '__main__':
    ex1 = TreeNode(3);
    ex1.left = TreeNode(9);
    ex1.right = TreeNode(20);
    ex1.right.right = TreeNode(15);
    ex1.left.left   = TreeNode(7);

    sol = Solution();
    print(sol.maxDepth(ex1));
