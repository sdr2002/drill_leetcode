import ipdb
dbg = ipdb.set_trace

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root is None:
            return True
        
        def isValid(node,smallest=None,biggest=None):
            if node is None:
                return True
            else:
                if not(smallest is None) and (node.val <= smallest):
                    return False
                elif not(biggest is None) and (node.val >= biggest):
                    return False
                else:                    
                    left_smallest = smallest
                    left_biggest  = node.val if (biggest is None) else min(node.val,biggest)
                    
                    right_smallest = node.val if (smallest is None) else max(node.val,smallest)
                    right_biggest  = biggest                                            
                        
                    if not(isValid(node.left,left_smallest,left_biggest)):
                        return False
                    elif not(isValid(node.right,right_smallest,right_biggest)):
                        return False
                    else:
                        return True
                
        #dbg()
        left_valid = isValid(root.left,None,root.val)
        right_valid = isValid(root.right,root.val,None)
        
        return left_valid and right_valid

if __name__ == "__main__":
    s = Solution()

    tn = None
    print(s.isValidBST(tn))

    tn = TreeNode(2)
    print(s.isValidBST(tn))

    tn = TreeNode(2)
    tn.left = TreeNode(1)
    tn.right = TreeNode(3)
    print(s.isValidBST(tn))

    tn = TreeNode(5)
    tn.left = TreeNode(1)
    tn.right = TreeNode(7)
    tn.right.left = TreeNode(3)
    tn.right.right = TreeNode(8)
    print(s.isValidBST(tn))

    tn = TreeNode(5)
    tn.left = TreeNode(1)
    tn.right = TreeNode(7)
    tn.right.left = TreeNode(6)
    tn.right.right = TreeNode(8)
    print(s.isValidBST(tn))
