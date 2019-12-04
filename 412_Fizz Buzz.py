import pdb;

def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    list_fb = []
    for i in range(1,n+1):
        if (i%3 == 0) and (i%5 == 0):
            additive = "FizzBuzz"
        elif (i%3 == 0) and (i%5 != 0):
            additive = "Fizz"
        elif (i%3 != 0) and (i%5 == 0):
            additive = "Buzz"
        else:
            additive = str(i)
        list_fb.append(additive)
        
    return list_fb


if __name__ == "__main__":
    print(fizzBuzz(3))

