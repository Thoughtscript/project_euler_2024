# https://projecteuler.net/problem=47
from lib import initialize, conclude, msg, prime_factorization
import time
from data import primes_to_2_mil_map

if __name__ == '__main__':

    try:

        result_data = initialize(47, 134043, 0, 0, [])

        PRIME_MAP = primes_to_2_mil_map.primes

        def number_of_divisors(num):
            prime_factors = prime_factorization(num)
            hm = {}

            for x in range(0, len(prime_factors), 1):
                n = prime_factors[x]

                if not hm.get(n) is None:
                    hm[n] = hm[n] + 1
                else:
                    hm[n] = 1

            return len(hm.keys())

        def solve(known_above):
            ALGO_BEGIN = time.time()

            for x in range(1, 999_999, 1):
                if x < known_above:
                    continue

                A = x
                B = x + 1
                C = x + 2
                D = x + 3

                msg(result_data, "Trying: " + str(A) + " " + str(B) + " " + str(C) + " " + str(D))

                NUM_A = number_of_divisors(A)
                if not NUM_A == 4:
                    continue

                NUM_B = number_of_divisors(B)
                if not NUM_B == 4:
                    continue

                NUM_C = number_of_divisors(C)
                if not NUM_C == 4:
                    continue

                NUM_D = number_of_divisors(D)
                if not NUM_D == 4:
                    continue

                if NUM_A == 4 and NUM_B == 4 and NUM_C == 4 and NUM_D == 4:
                    msg(result_data, "First four consecutive integers found with at least four distinct prime factors!")
                    conclude(result_data, A, ALGO_BEGIN)
                    return
            
        solve(134035) # 134043

    except Exception as ex:

        print('Exception: ' + str(ex))