import ipdb;

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        merged = MergedTreeNode(t1, t2);
        #ipdb.set_trace();
        merged.mergeTrees();
        #ipdb.set_trace();
        merged.setTreeNodeFromMergedTreeNode();
        #ipdb.set_trace();
        #return merged.getMergedTree();

        tree = merged.treeNode;
        return tree;
        
        
class MergedTreeNode(object):
    def __init__(self, tree1, tree2):
        
        self.ln1 = None if tree1 is None else tree1.left;
        self.ln2 = None if tree2 is None else tree2.left;
        self.rn1 = None if tree1 is None else tree1.right;
        self.rn2 = None if tree2 is None else tree2.right;        
        
        if (tree1 is None) and (tree2 is None):
            self.val = None;
        else:
            val1 = 0 if tree1 is None else tree1.val;
            val2 = 0 if tree2 is None else tree2.val;
            self.val = val1 + val2;

        self.left = None;
        self.right = None;

        self.treeNode = None;
        
    def mergeTrees(self):   
                
        if (self.ln1 is None) and (self.ln2 is None):
            pass;
        else:
            self.left = MergedTreeNode(self.ln1, self.ln2);
            self.left.mergeTrees();
        
        if (self.rn1 is None) and (self.rn2 is None):
            pass;
        else:
            self.right = MergedTreeNode(self.rn1, self.rn2);
            self.right.mergeTrees();
            
        return;

    def setTreeNodeFromMergedTreeNode(self):
        treeNode = TreeNode(self.val);

        if (self.left is None):
            treeNode.left = None;
        else:
            treeNode.left = self.left.setTreeNodeFromMergedTreeNode();

        if (self.right is None):
            treeNode.right = None;
        else:
            treeNode.right = self.right.setTreeNodeFromMergedTreeNode();

        self.treeNode = treeNode;
        return treeNode;   

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def set_tree_from_x_list(self, x_list):
        num_x = len(x_list);

        max_depth = 0;
        remained_nodes = int(num_x+0);
        is_max_depth_reached = False;
        while not(is_max_depth_reached):
            remained_nodes -= int(2**max_depth);
            if remained_nodes == 0:
                is_max_depth_reached = True;
            elif num_x < 0:
                raise Exception("Each depth of the tree must be fully defined");
            else:
                max_depth += 1;

        print('max_depth=%d'%max_depth)
        
        current_depth = 0;
        next_nodes = x_list[1:];
        
        last_depth = [];
        new_last_depth = [];

        for i in range(num_x):
            #pdb.set_trace();
            if i == 0:
                self.val = x_list[i];
                new_last_depth = [self];
                continue;
            else:
                if i >= int(2**(current_depth+1)-1):
                    current_depth += 1;
                    last_depth = [node for node in new_last_depth];
                    new_last_depth = [];

                x = x_list[i];
                index_parent_node = (i - (2**current_depth-1))//2;
                left_right = (i - (2**current_depth-1))%2;                

                new_node = TreeNode(x) if not(x is None) else None;
                parent_node = last_depth[index_parent_node];
                if parent_node is None:                    
                    assert new_node is None, "no-None child in None parent at i=%d?"%i;
                else:
                    if left_right == 0:
                        parent_node.left = new_node;
                        new_last_depth.append(parent_node.left);
                    else:
                        parent_node.right = new_node;
                        new_last_depth.append(parent_node.right);

    def get_ch_nodes(self):
        return [self.left, self.right];

    def get_ch_vals(self):
        return [None if self.left is None else self.left.val, None if self.right is None else self.right.val];

if __name__ == '__main__':
    ex1l = TreeNode(1); 
    ex1l.set_tree_from_x_list([1,3,2,5,None,None,None]);
    ex1r = TreeNode(None);
    ex1r.set_tree_from_x_list([2,1,3,None,4,None,7]);
    ipdb.set_trace();
    ex1=Solution();ex1.mergeTrees(ex1l,ex1r);
    print('Done!')
