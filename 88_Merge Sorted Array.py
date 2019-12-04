import ipdb
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ipdb.set_trace()

        if m == 0:
            nums1[:n] = nums2[:n]
        elif n == 0:
            pass
        else:
            max1 = max(nums1[:m])
            for xi in range(n):
                n2 = nums2[xi]

                bigger_than_max1 = True
                for xj in range(m):
                    n1 = nums1[xj]
                    if n2 <= n1:
                        nums1[xj+1:m+1] = nums1[xj:m]
                        nums1[xj] = n2
                        m+=1
                        bigger_than_max1 = False
                        break

                if bigger_than_max1:
                    nums1[m:m+(n-xi)] = nums2[xi:n]
                    break

        return nums1


if __name__ == '__main__':
    s = Solution()
    print( s.merge( [1,2,3,0,0,0],3,[2,5,6],3) ) # [1,2,2,3,5,6]
    print( s.merge( [0],0,[1],1 ) ) # [1]
    print( s.merge( [2,0],1,[1],1) ) # [1,2]
    print( s.merge( [1,0],1,[2],1) ) # [1,2]
