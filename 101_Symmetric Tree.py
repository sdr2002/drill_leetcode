from lib.BinaryTree import TreeNode

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.fn(root.left, root.right)

    def fn(self, nl, nr):
        if (nl is None) and (nr is None):
            return True
        elif not(nl is None) and (nr is None):
            return False
        elif (nl is None) and not(nr is None):
            return False
        else:
            if (nl.val == nr.val):
                return self.fn(nl.left,nr.right) and self.fn(nl.right, nr.left)
            else:
                return False
        

if __name__ == "__main__":
    s = Solution()    
    #tree.list_to_tree_breadth([1,2,3,7,8,5,2])
    tree = TreeNode(); tree.list_to_tree_breadth([1,2,2,3,4,4,3]); tree.print_tree();
    print(s.isSymmetric(tree),end='\n=======================\n\n')

    tree = TreeNode(); tree.list_to_tree_breadth([1,2,2,None,3,None,3]); tree.print_tree();
    print(s.isSymmetric(tree),end='\n=======================\n\n')
