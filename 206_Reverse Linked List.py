# Definition for singly-linked list.
import ipdb
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        arr = self.enum_nodes(head)
        return self.nodes_from_arr(arr[::-1])

    def enum_nodes(self,node):
        if node.next is None:
            return [node.val]
        else:
            return [node.val] + self.enum_nodes(node.next)

    def nodes_from_arr(self,arr):
        if len(arr) == 0:
            raise Exception('len 0 arr to nodify??')
        elif len(arr) == 1:
            return ListNode(arr[0])
        else:
            current_node = ListNode(arr[0])
            current_node.next = self.nodes_from_arr(arr[1:])
            return current_node

    def print_chain(self,chain):
        if chain.next is None:
            print('%d -> None\n'%chain.val)
        else:
            print('%d ->'%chain.val, end=' ')
            self.print_chain(chain.next)
            

if __name__ == '__main__':
    s = Solution()
    ex1 = s.nodes_from_arr([1,2,3,4]); s.print_chain(ex1);
    print(s.enum_nodes(ex1))    
    rev = s.reverseList(ex1); s.print_chain(rev);
    ipdb.set_trace()
