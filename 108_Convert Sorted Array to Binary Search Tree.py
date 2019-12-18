import ipdb
db = ipdb.set_trace
# Definition for a binary tree node.
from lib.BinaryTree import TreeNode

class Solution(object):
    """
    def sortedArrayToBST(self, nums):
        
        ns = len(nums)
        if ns == 0:
            return None
        else:
            head = TreeNode(nums[ns//2])
            if ns//2 >= 1:
                head.left = self.sortedArrayToBST(nums[:ns//2])
            else:
                head.left = None

            if ns > 1:
                head.right = self.sortedArrayToBST(nums[(ns//2)+1:])
            else:
                head.right = None
        
            return head
    """
    def sortedArrayToBST(self, nums):        
        def helper(left, right):
            if left > right:
                return None

            # always choose left middle node as a root
            p = (left + right) // 2

            # inorder traversal: left -> node -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root
        
        return helper(0, len(nums) - 1)
    
if __name__ == "__main__":
    
    s = Solution()
    db()
    tree = s.sortedArrayToBST([-10,-7,-3,-2,-1,0,2,4,5,9,13])
    tree.print_tree()
    #db()    
