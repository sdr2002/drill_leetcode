import pdb

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def iter_init(self,x_list):
        if (len(x_list)>0):
            self.val = x_list[0]
            if (len(x_list)==1):
                self.next = None
            else:
                self.next = ListNode(None)
                self.next.iter_init(x_list[1:])

    def iter_print(self):
        print(self.val, end=' ')
        if not(self.next is None):
            print('->', end=' ')
            self.next.iter_print()
        else:
            print('')
            return

class Solution(object):    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        self.merged = ListNode(None)
        
        def mg(lst1, lst2):
            v1 = None if (lst1 is None) else lst1.val
            v2 = None if (lst2 is None) else lst2.val
            
            node = ListNode(None)
            if not(v1 is None) and not(v2 is None):
                if (v1 <= v2):
                    node.val = v1
                    node.next = mg(lst1.next, lst2)
                else:
                    node.val = v2
                    node.next = mg(lst1, lst2.next)                
            elif not(v1 is None) and (v2 is None):
                node.val = v1
                node.next = mg(lst1.next, lst2)
            elif (v1 is None) and not(v2 is None):
                node.val = v2
                node.next = mg(lst1, lst2.next)
            else:
                node = None
            
            return node
        
        self.merged = mg(l1,l2)
        
        return self.merged

if __name__ == '__main__':

    s = Solution()

    l1 = ListNode(None)
    l1.iter_init([1,2,4])
    l2 = ListNode(None)
    l2.iter_init([1,3,4])

    mged = s.mergeTwoLists(l1,l2); mged.iter_print();
    pdb.set_trace()
