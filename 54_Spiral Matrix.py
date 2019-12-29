import ipdb
dbg = ipdb.set_trace

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])

                                       
        # loop( (0,1) -> (1,0) -> (0,-1) -> (-1,0) -> )
        noneArr = [None for i in range(n+2)]
        matrix = [noneArr] + [[None]+arr1d+[None] for arr1d in matrix] + [noneArr]
        
        arr1D = [None for i in range(m*n)]
        drc = 0; drcDict = {0:(0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)}
        ir = 1; ic = 1; cnt = 0;
        while cnt < m*n:
            arr1D[cnt] = matrix[ir][ic]
            matrix[ir][ic] = None
            dr, dc = drcDict[drc]
            if matrix[ir+dr][ic+dc] is None:
                drc = (drc+1)%4
                dr, dc = drcDict[drc]
            else:
                pass
            ir += dr
            ic += dc
            
            cnt += 1
            
        return arr1D

if __name__ == "__main__":
    s = Solution()
    arr1 = [
             [ 1, 2, 3 ],
             [ 4, 5, 6 ],
             [ 7, 8, 9 ]
           ]
    print(s.spiralOrder(arr1))
    
    arr2 = [
              [1, 2, 3, 4],
              [5, 6, 7, 8],
              [9,10,11,12]
           ]
    print(s.spiralOrder(arr2))

    print(s.spiralOrder([[]]))
