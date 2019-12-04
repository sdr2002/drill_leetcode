class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        count = 0;
        
        i = 2;
        primes = []
        while (i<n):            
            is_prime = True
            for p in primes:
                if i % p == 0:
                    is_prime = False

            if is_prime:
                print('%d is prime'%i)
                primes.append(i)

            i += 1
            
        return len(primes)
        

if __name__ == '__main__':
    s = Solution();
    print('---%d primes---'%s.countPrimes(100))
