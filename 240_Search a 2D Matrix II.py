import ipdb
dbg = ipdb.set_trace

from lib.BinarySearch import BinarySearch
BSAi = BinarySearch.binary_search_array_iteration

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n_v = len(matrix)
        if n_v == 0:
            return False
        else:
            n_h = len(matrix[0])
            
            n_diag = min(n_v,n_h)
            for i in range(0,n_diag):
                ind_h = BSAi(matrix[i][:i+1],target)
                if ind_h != -1:
                    return True
                
                ind_v = BSAi([v[i] for v in matrix[:i+1]],target)
                if ind_v != -1:
                    return True
                
            if n_v > n_h:
                for i in range(n_diag,n_v):
                    ind_h = BSAi(matrix[i],target)
                    if ind_h != -1:
                        return True
            elif n_v < n_h:
                for i in range(n_diag,n_h):
                    ind_v = BSAi([v[i] for v in matrix],target)
                    if ind_v != -1:
                        return True
            else:
                pass
            
            return False

if __name__ == "__main__":
    sol = Solution()
    prt = lambda **kwargs: print(sol.searchMatrix(**kwargs))

    #prt(matrix=[], target=0)
    #prt(matrix=[[]], target=0)

    arr1 = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    prt(matrix=arr1, target=20) # False
    prt(matrix=arr1, target=13) # True
    prt(matrix=arr1, target=43) # False
    prt(matrix=arr1, target=15) # True

    #dbg()
    arr2 = [
            [5,6,9],
            [9,10,13],
            [10,15,18]
           ]
    prt(matrix=arr2, target=9) # True
    prt(matrix=arr2, target=12) # False   
