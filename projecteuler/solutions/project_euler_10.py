# https://projecteuler.net/problem=10
from lib import initialize, msg, conclude
import time
from data import primes_to_2_mil_arr

if __name__ == '__main__':

    try:

        result_data = initialize(10, 142913828922, 0, 0, [])

        PRIMES = primes_to_2_mil_arr.primes

        def sum_below(mx):
            ALGO_BEGIN = time.time()

            result = 0
            for x in PRIMES:
                if x < mx:
                   result += x
            
            msg(result_data, "Sum of all values below " + str(mx) + " is " + str(result))
            conclude(result_data, result, ALGO_BEGIN)
   
        sum_below(2_000_000)

    except Exception as ex:

        print('Exception: ' + str(ex))