from lib.BinaryTree import TreeNode

import ipdb
dbg = ipdb.set_trace()

class Solution(object):
    def pathSum(self, root, sss):
        """
        :type root: TreeNode
        :type sss: int
        :rtype: int
        """
        def countPathsFromThis(node,cumsum):
            if node is None:
                return 0
            else:
                new_cumsum = cumsum + node.val
                if new_cumsum == sss:                    
                    return 1 + countPathsFromThis(node.left, new_cumsum) + countPathsFromThis(node.right, new_cumsum)
                else:
                    return 0 + countPathsFromThis(node.left, new_cumsum) + countPathsFromThis(node.right, new_cumsum)

        if root is None:
            return 0
        else:
            ch = countPathsFromThis(root,0)
            
            if root.left is None:
                cl = 0
            else:
                cl = self.pathSum(root.left, sss - root.val)

            if root.right is None:
                cr = 0
            else:
                cr = self.pathSum(root.right, sss - root.val)
                
            return ch + cl + cr
            
            
        
        if node.left is None:
            cl = 0
        else:
            cl = countPathsFromThis(node.left)
        if node.right is None:
            cr = 0
        else:
            cr = countPathsFromThis(node.right)
            
        return countPathsFromThis(node) + cl + cr


if __name__ == "__main__":
    s = Solution()
    dbg()
    tree = TreeNode()
    tree.list_to_tree_breadth([2,1,None])
    s.pathSum()
