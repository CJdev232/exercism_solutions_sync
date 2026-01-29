import math
def prime(number):
    if not number >= 1:
        raise ValueError('there is no zeroth prime')
    nthprimefinder = NthPrimeFinder(number)
    return nthprimefinder.find_nth_prime()
class NthPrimeFinder:
    def __init__(self,index_number):
        self._index_number = index_number
        self._primes_by_index = self._find_n_primes(self._index_number)
    def _find_factors(self,candidate):
        factors = []
        for divisor in range(1,math.floor(candidate**0.5)+1):
            if candidate % divisor == 0:
                factors.append(divisor)
        for factor in factors[::-1]:#this reversing would let final result natually sorted
            if factor != candidate // factor:#using // to try to avoid potential float issues
                factors.append(candidate // factor)
        return factors
        
    def _is_prime(self,candidate):
        factors_of_candidate = self._find_factors(candidate)
        return len(factors_of_candidate) == 2
        
    def _find_n_primes(self,count_target=1):
        candidate = 2
        count = 1
        primes = {}
        while count <= count_target:
            if self._is_prime(candidate):
                primes[count] = candidate
                count += 1 
            if candidate == 2:
                candidate = 3# except 2,all primes are odd numbers
            else:
                candidate += 2
        return primes

    def find_nth_prime(self):
        return self._primes_by_index[self._index_number]
    