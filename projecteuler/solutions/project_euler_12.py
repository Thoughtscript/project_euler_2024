# https://projecteuler.net/problem=12
from lib import initialize, conclude, msg
import time
from data import primes_to_2_mil_map

if __name__ == '__main__':

    try:

        result_data = initialize(12, 76_576_500, 0, 0, [])

        PRIME_MAP = primes_to_2_mil_map.primes

        def check_prime(num):
            SQ_RT = pow(num, 1/2)

            for x in range(2, SQ_RT+1, 1):
                if num % x == 0:
                    return False

            return True

        def prime_factorization(num):
            result = []
            rem = num

            while rem % 2 == 0:
                rem = rem / 2
                result.append(2)

            # Must be odd or not divisible by 2 once it reaches here
            for x in range(3, num+1, 2):
                if PRIME_MAP.get(x) is None and x <= 1999993:
                    continue

                if x > 1999993 and not check_prime(x):
                    continue

                while (rem % x == 0):
                    result.append(x)
                    rem = rem / x

                if rem == 1 or rem == 0:
                    break

            return result

        def number_of_divisors(num):
            prime_factors = prime_factorization(num)
            result = 1
            hm = {}

            for x in range(0, len(prime_factors), 1):
                n = prime_factors[x]

                if not hm.get(n) is None:
                    hm[n] = hm[n] + 1
                else:
                    hm[n] = 1

            keys = list(hm.keys())
            
            for x in range(0, len(keys), 1):
                n = hm[keys[x]]
                result = result * (n + 1)

            return result

        # Generates all triangular numbers up to num.
        # But all those not in the interval [min_num, max_num]
        def generate(num, min_num, max_num):
            lst = []
            last = 0
            for x in range(1,num+1,1):
                y = x + last
                last = y
                if y > min_num and y < max_num:
                    lst.append(y)

            return lst
        
        # ------------------------------------- #

        def solve(num):
            ALGO_BEGIN = time.time()

            # Cache these so they aren't repeatedly generated.
            triangulars = generate(num, 75_638_850, 100_000_000)
            num_with_most_factors = 1
            most_factors = 1

            for x in range(0, len(triangulars),1):
                TRI_NUM = triangulars[x]
                factors = number_of_divisors(TRI_NUM)
                msg(result_data, "Triangular Number: " + str(TRI_NUM) + " has number of factors: " + str(factors))

                if factors > most_factors:
                    most_factors = factors
                    num_with_most_factors = TRI_NUM
                    msg(result_data, "New largest num. of factors found: " + str(num_with_most_factors) + " with: " + str(most_factors))

                if factors > 500:
                    msg(result_data, "Triangular Number found: " + str(TRI_NUM) + " with number of factors: " + str(factors))
                    conclude(result_data, TRI_NUM, ALGO_BEGIN)
                    break

        solve(99_999)

        # New largest num. of factors found: 2031120 with: 240
        # New largest num. of factors found: 2162160 with: 320
        # New largest num. of factors found: 17907120 with: 480
        # Above: 75638850
        # Triangular Number: 76576500 has number of factors: 576

    except Exception as ex:
        print('Exception: ' + str(ex))