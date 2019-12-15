#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def make(self, ll):
        # ll: list of vals [1,0,0]
        if len(ll) == 0:
            return
        else:
            self.val = ll[0]
            if len(ll) > 1:
                self.next = ListNode(None)
                self.next.make(ll[1:])
            else:
                self.next = None
            return

import ipdb
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if (head is None):
            return True
        elif (head.next is None):
            return True
        else:
            prev = None
            n = 1
            while not(head.next is None):                
                head.prev = prev
                
                prev = head
                head = head.next
                
                n += 1
            head.prev = prev
            
            i = int(n)
            mid_i = n//2
            
            cur = head
            if n%2 == 1:
                #ipdb.set_trace()
                for x in range(mid_i):
                    cur = cur.prev
                cur = cur.prev
                cur.next = cur.next.next            
                n -= 1
            else:
                for x in range(mid_i):
                    cur = cur.prev
            #ipdb.set_trace()                
            while True:
                if (cur.val == cur.next.val):
                    if (cur.prev is None):
                        return True
                    else:
                        cur = cur.prev
                        cur.next = cur.next.next.next
                else:
                    return False
                
            
if __name__ == "__main__":
    s = Solution()
    
    ll=[]; test1 = ListNode(None); test1.make(ll);
    print('%r for %s'%(s.isPalindrome(test1),ll))

    ll=[1]; test1 = ListNode(None); test1.make(ll);
    print('%r for %s'%(s.isPalindrome(test1),ll))
    
    ll=[1,0,0]; test1 = ListNode(None); test1.make(ll);
    print('%r for %s'%(s.isPalindrome(test1),ll))

    ll=[1,0,0,1]; test1 = ListNode(None); test1.make(ll);
    print('%r for %s'%(s.isPalindrome(test1),ll))
            
    ll=[1,0,5,0,1]; test1 = ListNode(None); test1.make(ll);
    print('%r for %s'%(s.isPalindrome(test1),ll))

    ll=[1,2,5,0,1]; test1 = ListNode(None); test1.make(ll);
    print('%r for %s'%(s.isPalindrome(test1),ll))
