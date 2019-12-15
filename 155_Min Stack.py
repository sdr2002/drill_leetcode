class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.size = 2**10
        self.stack = [None for i in range(self.size)]
        self.top_ind = -1
        
        self.stale_min = True
        self.min_val = None
        
    def check_size(self):
        if self.size-1 == self.top_ind:
            print('Stack is full!')
            self.stack.extend([None for i in range(self.size)])
            self.size *= 2
        elif (self.top_ind >= 127) and ((self.size//2 -1) - 1 > self.top_ind):
            print('Stack is too big!')
            self.size = self.size // 2
            self.stack = self.stack[:self.size]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.check_size()
        
        self.stack[self.top_ind+1] = x
        self.top_ind += 1
        
        self.stale_min = True

    def pop(self):
        """
        :rtype: None
        """
        if self.top_ind < 0:
            return
        else:
            self.stack[self.top_ind] = None
            self.top_ind -= 1
            
            self.stale_min = True

    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.top_ind]        

    def getMin(self):
        """
        :rtype: int
        """
        if self.stale_min:
            min_val = None
            for i in range(self.top_ind+1):
                if min_val is None:
                    min_val = self.stack[i]
                else:
                    if min_val > self.stack[i]:
                        min_val = self.stack[i]

            self.stale_min = False
            self.min_val = min_val
            return min_val
        else:
            return self.min_val

    def get_list(self):
        return self.stack[:self.top_ind+1]

if __name__ == '__main__':
    import ipdb
    m = MinStack()

    ipdb.set_trace()
    print('0')

    m.push(-2)
    m.push(0)
    m.push(-3)
    print(m.get_list())
    print(m.getMin())
    m.pop()
    print(m.top())
    print(m.get_list())
    print(m.getMin())
    
