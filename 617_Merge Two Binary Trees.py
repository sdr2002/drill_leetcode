import ipdb;

from lib.BinaryTree import TreeNode

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

if __name__ == '__main__':
    s=Solution();

    ex1l = TreeNode(); 
    ex1l.list_to_tree_breadth([1,3,2,5,None,None,None]);
    ex1r = TreeNode();
    ex1r.list_to_tree_breadth([2,1,3,None,4,None,7]);
    ex1l.print_tree()
    ex1r.print_tree()

    ipdb.set_trace();
    ex1= s.mergeTrees(ex1l,ex1r);

    ex1.print_tree()
