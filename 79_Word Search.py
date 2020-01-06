import ipdb
dbg = ipdb.set_trace

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        num = len(word)
        if num==0:
            return True
        
        m = len(board)
        if m ==0:
            return False        
        n = len(board[0])
        if n ==0:
            return False
        
        if num > m*n:
            return False
        
        ch = word[0]
        inits = []
        
        for ir in range(m):
            for ic in range(n):
                if board[ir][ic] == ch:
                    inits.append((ir,ic))

        if not(inits):
            return False
        elif (num == 1) and inits:
            return True

        
        def search(path,ind):
            next_ch = word[ind]
            
            ir,ic = path[-1]
            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                if ir+dr < 0 or ir+dr >=m:
                    continue
                elif ic+dc < 0 or ic+dc >=n:
                    continue
                elif (ir+dr,ic+dc) in path:
                    continue
                else:
                    if board[ir+dr][ic+dc] == next_ch:
                        if ind >= num-1:
                            return True
                        else:                            
                            isExist = search(path+[(ir+dr,ic+dc)],ind+1)
                            if isExist:
                                return True
                            else:
                                continue
                    else:
                        continue
            return False
        
        dbg() 
        for ir,ic in inits:
            ret = search([(ir,ic)],1)
            if ret:
                return True
            else:
                continue
        return False

if __name__ == "__main__":
    sol = Solution()
    prt = lambda **kwargs: print(sol.exist(**kwargs))

    board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

    #prt(board=board,word="ABCCED") # True

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] # True
    #prt(board=board,word="SEE")

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] # False
    prt(board=board,word="ABCB")
