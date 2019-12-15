import ipdb

idbg = ipdb.set_trace

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

    def list_to_tree_breadth(self,x_list):
        #idbg()
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
                #idbg()
                depth += 1
                ind = 0
            else:
                ind += 1
        print("--------------")
        return


if __name__ == "__main__":
    tree = TreeNode()
    #tree.list_to_tree_breadth([1,2,3,7,8,5,2])
    tree.list_to_tree_breadth([1,2,3,None,7,5,2,None,None,1,None,None,1,2,3])
    tree.print_tree()
    idbg()
    tree = TreeNode()
    tree.list_to_tree_breadth([1,None,3,None,None,5,2,None,None,None,None,None,1,2,3])
    tree.print_tree()
    print('Done')
