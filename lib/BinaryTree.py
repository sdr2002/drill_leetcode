import ipdb

dbg = ipdb.set_trace

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

    def list_to_tree_breadth(self,x_list):
        parents = [self]
        # Test if length of x_list is valid: len(x_list) must be 2**N-1
        if len(x_list)==0:
            pass
        else:
            two_power = len(x_list)+1
            while(two_power>1):                
                assert (two_power%2 == 0), "x_list has invalid length"
                two_power //= 2

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
                #dbg()
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

    def delete_node(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        
        def find_node_to_delete(parent_of_node,node,key):
            if node is None:
                return parent_of_node, None
            else:
                if node.val > key:
                    if node.left is None:
                        return parent_of_node, None
                    else:
                        return find_node_to_delete(node,node.left,key)
                elif node.val < key:
                    if node.right is None:
                        return parent_of_node, None
                    else:
                        return find_node_to_delete(node,node.right,key)
                else:
                    return parent_of_node,node
        
        parent_of_head, head = find_node_to_delete(root,root,key)
        dbg()
        if (head is None):
            return root            
        else:           
            lnd = head.left
            rnd = head.right

            if (lnd is None) and (rnd is None):
                if parent_of_head == head:
                    return None
                else:
                    new_node = self.insert_node(lnd,rnd)
                    if not(parent_of_head.left is None) and (parent_of_head.left.val == head.val):
                        parent_of_head.left = new_node
                    elif not(parent_of_head.right is None) and (parent_of_head.right.val == head.val):
                        parent_of_head.right = new_node
                    else:
                        raise Exception("child val should exist! 2")                        
                    return root
            else:
                new_node = self.insert_node(lnd,rnd)
                if parent_of_head == head:
                    return new_node
                else:                
                    if not(parent_of_head.left is None) and (parent_of_head.left.val == head.val):
                        parent_of_head.left = new_node
                    elif not(parent_of_head.right is None) and (parent_of_head.right.val == head.val):
                        parent_of_head.right = new_node
                    else:
                        raise Exception("child val should exist! 2")
                    return root
        
                
    def insert_node(self, root, new_nd):
        """
        :type root: TreeNode
        :type new_nd: TreeNode
        :rtype: TreeNode
        """
        def search(node,new_nd):
            if node is None:
                return new_nd
            elif new_nd is None:
                return node
            else:
                if node.val > new_nd.val:
                    if node.left is None:
                        node.left = new_nd
                        return None
                    else:
                        _ = search(node.left,new_nd)
                elif node.val < new_nd.val:
                    if node.right is None:
                        node.right = new_nd
                        return None
                    else:
                        _ = search(node.right,new_nd)                    
                        return None
                else:
                    return None # will change if node contains items except value
        new_root = search(root,new_nd)
        if new_root is None:
            return root
        else:
            return new_root
        
    
    def insert_node_by_val(self, root, val):
        return self.insert_node(root,TreeNode(val))

def test_delete_node():
    print("Test tree deletion~~~~~~~~~~~~~~~~~~~~~~")
    tree = TreeNode()
    tree.list_to_tree_breadth([0])
    #dbg()
    new_tree = tree.delete_node(tree,0)
    assert new_tree is None, "Not None!"
    #dbg()
    
    tree = TreeNode()
    tree.list_to_tree_breadth([1])
    #dbg()
    new_tree = tree.delete_node(tree,0)
    new_tree.print_tree()
    #dbg()

    tree = TreeNode()
    tree.list_to_tree_breadth([1,None,2])
    tree.print_tree()
    dbg()
    new_tree = tree.delete_node(tree,1)
    new_tree.print_tree()
    dbg()

    tree = TreeNode()
    tree.list_to_tree_breadth([1,None,2])
    tree.print_tree()
    dbg()
    new_tree = tree.delete_node(tree,2)
    new_tree.print_tree()
    dbg()    

    tree = TreeNode()
    tree.list_to_tree_breadth([2,1,None])
    tree.print_tree()
    dbg()
    new_tree = tree.delete_node(tree,2)
    new_tree.print_tree()
    dbg()

    return True
if __name__ == "__main__":
    """
    print("\n\n~~~~Tree gen list by depth~~~~")
    tree = TreeNode()
    tree.list_to_tree_breadth([2\
                                ,1,33\
                                ,None,None,25,40\
                                ,None,None,None,None,11,None,34,None\
                                ,None,None,None,None,None,None,None,None,7,12,None,None,None,36,None,None])
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

    print("\n\n~~~~Tree delete~~~~")
    tree = TreeNode()
    tree.list_to_tree_breadth([5,3,6,2,4,None,7])
    #dbg()
    new_tree = tree.delete_node(tree,3)
    new_tree.print_tree()
    #dbg()
    """

    tree = TreeNode()
    tree.list_to_tree_breadth([0])
    #dbg()
    new_tree = tree.delete_node(tree,0)
    assert new_tree is None, "Not None!"
    #dbg()
    
    tree = TreeNode()
    tree.list_to_tree_breadth([1])
    #dbg()
    new_tree = tree.delete_node(tree,0)
    new_tree.print_tree()
    #dbg()

    tree = TreeNode()
    tree.list_to_tree_breadth([1,None,2])
    tree.print_tree()
    dbg()
    new_tree = tree.delete_node(tree,1)
    new_tree.print_tree()
    dbg()

    tree = TreeNode()
    tree.list_to_tree_breadth([1,None,2])
    tree.print_tree()
    dbg()
    new_tree = tree.delete_node(tree,2)
    new_tree.print_tree()
    dbg()    

    tree = TreeNode()
    tree.list_to_tree_breadth([2,1,None])
    tree.print_tree()
    dbg()
    new_tree = tree.delete_node(tree,2)
    new_tree.print_tree()
    dbg()

    test_delete_node()
