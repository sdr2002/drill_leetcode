class BinarySearch(object):
    @staticmethod
    def binary_search_array_iteration(arr,val):
        """
        Binary search on an array using a loop: return index at the array if the val exists, -1 else
        See __main__ for examples
        """
        num = len(arr)
        if num == 0:
            return -1        
        ind_l = 0; ind_r = num-1;

        while (ind_r >= ind_l):
            ind_mid = (ind_l + ind_r)//2
            if val < arr[ind_mid]:
                ind_r = ind_mid-1
            elif val > arr[ind_mid]:
                ind_l = ind_mid+1
            else:
                return ind_mid
        return -1

    @staticmethod
    def binary_search_array_recursion(arr,val):
        """
        Binary search on an array using recursion: return index at the array if the val exists, -1 else
        """
        num = len(arr)
        if num == 0:
            return -1

        def recursion(il,ir):
            if il > ir:
                return -1
            else:
                ind_mid = (il + ir)//2
                if val < arr[ind_mid]:
                    ind = recursion(il,ind_mid-1)
                elif val > arr[ind_mid]:
                    ind = recursion(ind_mid+1,ir)
                else:
                    ind = ind_mid
                return ind

        ind_l = 0; ind_r = num-1;      
        return recursion(ind_l,ind_r)

BSAi = BinarySearch.binary_search_array_iteration
BSAr = BinarySearch.binary_search_array_recursion

if __name__ == "__main__":
    
    print("----Iteration----")
    print(BSAi([],2)) # -1
    print(BSAi([1,3,6,7,10,11,13],6)) # 2
    print(BSAi([1,3,6,7,10,11,13],5)) # -1
    print(BSAi([1,3,6,7,10,11,13],11)) # 5
    print(BSAi([1],11)) # -1
    print(BSAi([1],1)) # 0

    print("----Recursion----")
    print(BSAr([],2)) # -1
    print(BSAr([1,3,6,7,10,11,13],6)) # 2
    print(BSAr([1,3,6,7,10,11,13],5)) # -1
    print(BSAr([1,3,6,7,10,11,13],11)) # 5
    print(BSAr([1],11)) # -1
    print(BSAr([1],1)) # 0
