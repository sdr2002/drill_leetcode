import ipdb
dbg = ipdb.set_trace

class Node(object):
    def __init__(self,ind,candies,keys=None,children=None):
        self.ind      = ind
        self.candies  = candies

        self.keys     = keys # list() of int (indecies)
        self.children = children # list() of Nodes
        

class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """

        if len(initialBoxes)==0:
            return 0

        n_candies = 0

        head = Node(len(status),0)     
        containedBoxes.append(initialBoxes)
        keys.append([])

        node = head
        def build_tree(node, prev_keys, prev_boxes):
            #dbg()
            prev_keys.update(keys[node.ind])
            prev_boxes.update([node.ind])

            children_inds = containedBoxes[node.ind]
            node.children = None if len(children_inds)==0 else [Node(ind,candies[ind],keys[ind]) for ind in children_inds]

            if not(node.children is None):
                for ch in node.children:
                    if (status[ch.ind]==1) or (ch.ind in prev_keys):
                        prev_keys, prev_boxes = build_tree(ch,prev_keys,prev_boxes)
            
            return prev_keys, prev_boxes           

        all_keys = set(); all_boxes = set();
        n_keys = 0; n_boxes = 0;
        while True:
            all_keys, all_boxes = build_tree(head, all_keys, all_boxes)
            #dbg()
            if (n_keys == len(all_keys)) and (n_boxes == len(all_boxes)):
                break
            else:
                n_keys = len(all_keys); n_boxes = len(all_boxes);
        #dbg()

        for i in range(len(status)):
            if i in all_boxes:
                if (status[i] == 1) or (i in all_keys):
                    n_candies += candies[i] 

        return n_candies


if __name__ == "__main__":
    sol=Solution().maxCandies
    prt = lambda **kwargs: print(sol(**kwargs))
    
    prt(status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0])
    prt(status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0])
    prt(status = [1,1,1], candies = [100,1,100], keys = [[],[0,2],[]], containedBoxes = [[],[],[]], initialBoxes = [1])
    prt(status = [1], candies = [100], keys = [[]], containedBoxes = [[]], initialBoxes = [])
    prt(status = [1,1,1], candies = [2,3,2], keys = [[],[],[]], containedBoxes = [[],[],[]], initialBoxes = [2,1,0])
