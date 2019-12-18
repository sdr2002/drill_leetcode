import ipdb

db = ipdb.set_trace

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

    def list_to_tree_breadth(self,x_list):
        #db()
        parents = [self]
        # [1 || 2,3 || None,7,5,2 || None,None,1,None,None,1,2,3]
        while not(all([p is None for p in parents])) and not(len(x_list)==0):
            nd = parents.pop(0)
            if not(nd is None): # If not None node
                nd.val = x_list.pop(0)
                if len(parents) < len(x_list):
                    if (len(x_list)>0) and not(x_list[len(parents)] is None):
                        nd.left = TreeNode()
                        parents.append(nd.left)
                    else:
                        parents.append(None)

                    if (len(x_list)>1) and not(x_list[len(parents)] is None):
                        nd.right = TreeNode()
                        parents.append(nd.right)
                    else:
                        parents.append(None)
                else:
                    #leaf node, pass
                    nd.left = None; nd.right = None;
            else: # None node, fill None to queue
                _ = x_list.pop(0)
                parents.extend([None,None])                

        return

    def print_node(self,isTree=False):
        ender = '' if isTree else '\n'
        if self.val is None:
            print("||None", end=ender)
        else:
            print("||%d"%self.val, end=ender)
        return

    def print_tree(self):
        print("-----Tree-----")
        parents = [self]
        depth = 0
        ind = 0        
        while not(len(parents)==0) and (not(all([p is None for p in parents])) or ind!=0):
            nd = parents.pop(0)
            if not(nd is None):
                nd.print_node(True)
                parents.append(nd.left)           
                parents.append(nd.right)
            else:
                print("||None", end='')
                parents.extend([None, None])

            if ind == 2**depth - 1:
                print('||\n')
                #db()
                depth += 1
                ind = 0
            else:
                ind += 1
        print("--------------")
        return

    @staticmethod    
    def tree_to_list_inorder(root):
        return [] if (root is None) else TreeNode.tree_to_list_inorder(root.left) + [root.val] + TreeNode.tree_to_list_inorder(root.right)

    @staticmethod
    def list_to_tree_depth_inorder(x_list):
        """
        LeetCode 108.Convert Sorted Array to Binary Search Tree
        : https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
        """
        x_list = sorted([x for x in x_list if not(x is None)])
        def helper(left, right):
            if left > right:
                return None
            else:
                # always choose left middle node as a root
                p = (left + right) // 2

                # inorder traversal: left -> node -> right
                root = TreeNode(x_list[p])
                root.left = helper(left, p - 1)
                root.right = helper(p + 1, right)
                return root
        
        return helper(0, len(x_list) - 1)

    @staticmethod
    def is_tree_balanced(root):            
        """
        LeetCode 110.Balanced Binary Tree
        : https://leetcode.com/problems/balanced-binary-tree/
        """
        if root is None:
            return True
        else:
            def compare(node):
                """
                In: node
                Out: bool is_bal / max_depth
                """
                if node is None:
                    return True, 0
                else:
                    _l, max_depth_l = compare(node.left)
                    _r, max_depth_r = compare(node.right)
                
                if (_l is False) or (_r is False):
                    return False, -(2**32)
                elif abs(max_depth_l - max_depth_r)<=1:
                    return True, max(max_depth_l,max_depth_r)+1
                else:
                    return False, -(2**32)
                
            is_bal, depth = compare(root)
            return is_bal

if __name__ == "__main__":
    print("\n\n~~~~Tree gen list by depth~~~~")    
    tree = TreeNode()
    tree.list_to_tree_breadth([2\
                                ,1,33\
                                ,None,None,25,40\
                                ,None,None,None,None,11,None,34,None\
                                ,None,None,None,None,None,None,None,None,7,12,None,None,None,36,None,None,None,None])
    tree.print_tree()
    print(TreeNode.tree_to_list_inorder(tree))
    

    print("\n\n~~~~Tree gen from list by depth inorder~~~~")
    tree = TreeNode()    
    tree = TreeNode.list_to_tree_depth_inorder([1,2,7,11,12,13,25,33,34,36,40])    
    tree.print_tree()
    print(TreeNode.tree_to_list_inorder(tree))


    print("\n\n~~~~Rebalance Tree inorder~~~~")
    tree = TreeNode(10)
    tree.left = TreeNode(8)
    tree.left.left = TreeNode(7)
    tree.left.left.left = TreeNode(6)
    tree.left.left.left = TreeNode(5)
    tree.print_tree()
    print("Balance: %r"%TreeNode.is_tree_balanced(tree))
    print("=>")
    vlist = TreeNode.tree_to_list_inorder(tree)
    tree = TreeNode.list_to_tree_depth_inorder(vlist)
    tree.print_tree()
    print("Balance: %r"%TreeNode.is_tree_balanced(tree))


