import ipdb

dbg = ipdb.set_trace

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        grid = [[int(c) for c in arr1] for arr1 in grid]
        
        d0 = len(grid)
        if d0 == 0:
            return 0
        d1 = len(grid[0])
        
        n_ones = sum([sum(arr1) for arr1 in grid])
        count_ones = 0        
        
        def search_row_col(row,col,cnt1):
            if (row < 0) or (col < 0):
                return cnt1
            elif (row >= d0) or (col >= d1):
                return cnt1
            else:
                if grid[row][col] == 1:
                    cnt1 += 1
                    grid[row][col] = 0
                    
                    cnt1 = search_row_col(row-1,col,cnt1)
                    cnt1 = search_row_col(row+1,col,cnt1)
                    cnt1 = search_row_col(row,col-1,cnt1)
                    cnt1 = search_row_col(row,col+1,cnt1)
                
                return cnt1
 
        num_island = 0
        while count_ones < n_ones:
            for i in range(d0):
                for j in range(d1):
                    if grid[i][j] == 1:
                        count_ones = search_row_col(i,j,count_ones)
                        num_island += 1
                        
        return num_island
        
if __name__ == "__main__":
    s = Solution()

    dbg()
    grid = [['1']]
    print(s.numIslands(grid))

    dbg()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(s.numIslands(grid))

    dbg()
    grid = [[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]
    print(s.numIslands(grid))

    dbg()
    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]
    print(s.numIslands(grid))
