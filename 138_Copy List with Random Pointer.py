import ipdb

dbg = ipdb.set_trace


# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        else:
            dict_nodes = dict()
            nodes_hash = dict()
            ind = 0

            dbg()
            search_1st = head
            while not(search_1st is None):
                dict_nodes[search_1st] = ind
                nodes_hash[ind] = Node(search_1st.val, next=None, random=None)
                if ind != 0:
                    nodes_hash[ind-1].next = nodes_hash[ind]
                ind += 1    
                search_1st = search_1st.next

            dbg()
            search_2nd = head
            ind = 0
            while not(search_2nd is None):
                rand_node = search_2nd.random

                if rand_node is None:
                    pass
                else:
                    rand_ind = dict_nodes[rand_node]
                    nodes_hash[ind].random = nodes_hash[rand_ind]
                    pass

                ind += 1
                search_2nd = search_2nd.next
                
            return nodes_hash[0]

def list_to_rand_node(lst):
    n = len(lst)
    nodes_hash = dict()
    for ind in range(n):
        nodes_hash[ind] = Node(lst[ind][0])

    for ind in range(n):
        if ind < n-1:
            nodes_hash[ind].next = nodes_hash[ind+1]

        rand_ind = lst[ind][1]
        if rand_ind is None:
            nodes_hash[ind].random = None
        else:
            rand_node = nodes_hash[rand_ind]
            nodes_hash[ind].random = rand_node

    return nodes_hash[0]

if __name__ == "__main__":
    s = Solution()
    head = s.copyRandomList(list_to_rand_node([[7,None],[13,0],[11,4],[10,2],[1,0]]))
    dbg()
