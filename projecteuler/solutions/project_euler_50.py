# https://projecteuler.net/problem=50
from lib import initialize, msg, conclude, list_to_map
import time
from data import primes_to_2_mil_arr

if __name__ == '__main__':

    try:
        result_data = initialize(50, 997651, 0, 0, [])

        PRIMES = primes_to_2_mil_arr.primes
        PRIME_MAP = list_to_map(PRIMES)
 
        def solve():
            ALGO_BEGIN = time.time()

            mx_num = 0

            solution = -1

            # 2, 3, 5, 7, 11, 13, ...
            # left-pointer
            for x in range(0, len(PRIMES), 1):
                sum = 0
                temp = []
                if PRIMES[x] >= 1_000_000:
                    break

                for y in range(x, len(PRIMES), 1):
                    NEXT_NUM = sum + PRIMES[y]
                    if NEXT_NUM >= 1_000_000:
                        break

                    temp.append(PRIMES[y])
                    sum = NEXT_NUM

                    IS_PRIME = not PRIME_MAP.get(NEXT_NUM) is None
                    if IS_PRIME:
                        if (mx_num < len(temp)):
                            mx_num = len(temp)
                            msg(result_data, "New max length found: " + str(len(temp)) + " for prime " + str(NEXT_NUM))
                            solution = NEXT_NUM
                                   
            conclude(result_data, solution, ALGO_BEGIN)

        solve() # 997651

    except Exception as ex:

        print('Exception: ' + str(ex))