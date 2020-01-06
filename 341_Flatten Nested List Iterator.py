import ipdb
dbg = ipdb.set_trace
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self._ls = nestedList
        self._flatten = []
        _next = pop_nested(self._ls)
        while not(_next is None):
            self._flatten.append(_next)
            _next = pop_nested(self._ls)                

    def next(self):
        """
        :rtype: int
        """
        if len(self._flatten) > 0:
            return self._flatten.pop(0)
        else:
            return None

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self._flatten) > 0:
            return True
        else:
            False

def pop_nested(lst,depth=0):
    ret = None
    #dbg()
    if lst == []:
        return None
    while (ret is None) and (lst != []):
        entry = lst[0]
        if isinstance(entry,int):
            lst.pop(0)
            return entry
        elif isinstance(entry,list):
            if entry == []:
                lst.pop(0)
                if depth != 0:
                    return None
                else:
                    pass
            else:
                ret = pop_nested(entry,depth+1)
    return ret

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

if __name__ == "__main__":

    test = []
    i, v = NestedIterator(test), []
    while i.hasNext(): v.append(i.next())
    print(v)

    test = [[[[]]]]
    i, v = NestedIterator(test), []
    while i.hasNext(): v.append(i.next())
    print(v)

    test = [[ [[],[],[]] ,[[],[],[]] ]]
    i, v = NestedIterator(test), []
    while i.hasNext(): v.append(i.next())
    print(v)

    test = [1,2]
    i, v = NestedIterator(test), []
    while i.hasNext(): v.append(i.next())
    print(v)

    test = [[[],1],2]
    i, v = NestedIterator(test), []
    while i.hasNext(): v.append(i.next())
    print(v)

    test = [[[0,[]],1],2]
    i, v = NestedIterator(test), []
    while i.hasNext(): v.append(i.next())
    print(v)

    test = [[1,1],2,[1,1]]
    i, v = NestedIterator(test), []
    while i.hasNext(): v.append(i.next())
    print(v)
