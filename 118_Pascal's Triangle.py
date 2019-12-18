import ipdb
idb = ipdb.set_trace

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        arr2d = [None for i in range(numRows)]
        
        for ri in range(1,numRows+1):
            arr = [None for j in range(ri)]
            arr[0] = 1; arr[-1] = 1;
            if ri > 2:
                pastarr = arr2d[ri-2]
                for ci in range(1,ri-1):
                    arr[ci] = pastarr[ci-1]+pastarr[ci]
            arr2d[ri-1] = arr
            
        return arr2d


if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))
