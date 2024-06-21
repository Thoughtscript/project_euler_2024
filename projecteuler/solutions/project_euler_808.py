# https://projecteuler.net/problem=808
from lib import initialize, conclude, msg
import time
import math
from data import primes_to_100_mil_map, primes_to_100_mil_arr

if __name__ == '__main__':

    try:

        result_data = initialize(808, 3807504276997394, 0, 0, [])

        PRIME_MAP = primes_to_100_mil_map.primes
        PRIMES = primes_to_100_mil_arr.primes

        def check_prime(num_str):
            num = int(num_str)

            SQ_RT = pow(num, 1/2)

            if PRIME_MAP.get(SQ_RT) is None:
                return False

            return True

        # If not palindrome forward, not palindrome backwards.
        def is_palindrome(num_str):
            LEN = len(num_str)
            HALF = int(math.floor(len(num_str) / 2))

            if LEN == 1:
                return True

            for x in range(0, HALF, 1):
                if num_str[x] == num_str[LEN - 1 - x]:
                    continue

                else:
                    return False
            
            return True

        # No guarantee that reversed num is also in lowest/first 50 for probably 10+ such.
        def reverse_num_str(num_str):
            result = ''

            for x in range(len(num_str) - 1, -1, -1):
                result += num_str[x]

            return result

        def is_reversible_prime_square(num_str):
            if not is_palindrome(num_str):
 
                reversed = reverse_num_str(num_str)
                if not check_prime(int(reversed)):
                    return False
                
                return int(num_str)
            return False

        def solve():
            ALGO_BEGIN = time.time()

            count = 0
            total = 0

            for x in range(0, len(PRIMES), 1):
                if (count == 50):
                    break

                squared = int(math.pow(PRIMES[x], 2))

                to_sum = is_reversible_prime_square(str(squared))

                if to_sum:
                    msg(result_data, str(to_sum) + " reversible prime square found!")
                    count += 1
                    total += to_sum

            msg(result_data, str(count) + " reversible prime squares found! " + str(total) + " resulting sum")
            conclude(result_data, total, ALGO_BEGIN)

        solve() # 3807504276997394

    except Exception as ex:

        print('Exception: ' + str(ex))
