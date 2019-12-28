import ipdb
dbg = ipdb.set_trace

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        if n < 2:
            return intervals
        else:
            intervals = [intervals[i] for i in sorted(range(n), key= lambda k: intervals[k])]

            reduced = [intervals[0]]
            num = len(intervals)        
            for i in range(num):
                sub = intervals[i]
                nred = len(reduced)
                merged = False
                for j in range(nred):                
                    if self.isOverlap(reduced[j],sub):
                        reduced[j] = self.mergeTwo(reduced[j],sub)
                        merged = True
                        break
                        
                if not(merged):
                    reduced.append(sub)
                    
            return reduced
        
    def isIn(self,intv,v):
        return (intv[0]<=v) and (intv[1]>=v)
    
    def isOverlap(self,intv1,intv2):
        return self.isIn(intv1,intv2[0]) or self.isIn(intv1,intv2[1]) or self.isIn(intv2,intv1[0]) or self.isIn(intv2,intv1[1])
    
    def mergeTwo(self,intv1,intv2):
        left  = min(intv1[0],intv2[0])
        right = max(intv1[1],intv2[1])         
        return [left,right]


if __name__ == "__main__":
    s = Solution()
    print(s.merge( [[1,3],[2,6],[8,10],[15,18]] )) # [[1,6],[8,10],[15,18]]
    print(s.merge( [[1,3],[5,10],[2,6]] )) # [[1,10]]
    print(s.merge( [[1,3]] )) # [[1,10]]
    print(s.merge( [[]] )) # [[1,10]]
