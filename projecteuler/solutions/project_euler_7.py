# https://projecteuler.net/problem=7
from lib import initialize, conclude
import time
from data import primes_to_2_mil_arr

if __name__ == '__main__':

    try:

        result_data = initialize(7, 104743, 0, 0, [])

        PRIMES = primes_to_2_mil_arr.primes
        
        def solve():
            ALGO_BEGIN = time.time()

            solution = PRIMES[10_000]
            
            conclude(result_data, solution, ALGO_BEGIN)

        solve() # 104743

    except Exception as ex:
        print('Exception: ' + str(ex))