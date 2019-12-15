import ipdb
idbg = ipdb.set_trace

class Solution(object):
    def intersect(self,nums1,nums2):
        d1 = dict()
        d2 = dict()

        def get_heap(nums):
            dd = dict()
            for v in nums:
                if v in dd.keys():
                    dd[v] += 1
                else:
                    dd[v]  = 1
            return dd

        d1 = get_heap(nums1)
        d2 = get_heap(nums2)

        arr = [None for i in range(min(len(nums1),len(nums2)))]
        i_arr = 0

        #idbg()

        for k1 in d1.keys():
            if k1 in d2.keys():
                for i in range(min(d1[k1],d2[k1])):
                    arr[i_arr] = k1
                    i_arr += 1

        return arr[:i_arr]


    def intersect_sort(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        # make n1 < n2
        if n1 > n2:
            temp = nums1
            nums1 = nums2
            nums2 = temp
            
            temp = n1
            n1 = n2
            n2 = temp
            
            del temp
            
        arr = [None for i in range(n1)]
        larr = 0

        #idbg()
        while (len(nums1) > 0) and (len(nums2) > 0):
            e1 = nums1[0]
            e2 = nums2[0]
            
            if e1 == e2:
                arr[larr] = int(e1)
                larr += 1
                nums1.pop(0)
                nums2.pop(0)
            elif e1 < e2:
                nums1.pop(0)
            else:
                nums2.pop(0)                        
            
        return arr[:larr]

if __name__ == "__main__":
    s = Solution()
    print(s.intersect([1,2,2,1],[2,2]))
    print(s.intersect([4,9,5],[9,4,9,8,4]))
