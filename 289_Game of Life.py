class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        orig = [[v for v in lst1d] for lst1d in board]
        
        nrow = len(board)
        ncol = len(board[0])
        for row in range(nrow):
            for col in range(ncol):
                state = orig[row][col]
                n_neighbours = self.get_nb(row,col,orig,nrow,ncol)
                
                if state == 1:
                    if n_neighbours < 2:
                        board[row][col] = 0
                    elif n_neighbours < 4:
                        board[row][col] = 1
                    else:
                        board[row][col] = 0
                else:
                    if n_neighbours == 3:
                        board[row][col] = 1
                
    def get_nb(self,row,col,orig,nrow,ncol):
        n_neighbours = 0
        for drow in [-1,0,1]:
            for dcol in [-1,0,1]:
                if drow == dcol == 0:
                    continue
                else:
                    if (row+drow < 0) or (row+drow >= nrow):
                        continue
                    elif (col+dcol <0) or (col+dcol >= ncol):
                        continue
                    else:
                        n_neighbours += orig[row+drow][col+dcol]
                        
        return n_neighbours
