# https://projecteuler.net/problem=27
from lib import initialize, conclude, msg
import time
import math
from data import primes_to_2_mil_map

if __name__ == '__main__':

    try:
        result_data = initialize(27, -59231, 0, 0, [])

        PRIME_MAP = primes_to_2_mil_map.primes

        def check_prime(num):
            if PRIME_MAP.get(num) is None:
                return False
            return True

        def formula(n, a, b):
            return math.pow(n, 2) + a * n + b

        def solve():
            ALGO_BEGIN = time.time()

            mx = 0
            coefficient_prod = 0

            for a in range(-999, 999, 1):
                for b in range(-1000, 1001, 1):
                    seq_len = 0
                    for n in range(0, 81, 1):
                        formula_out = formula(n, a, b)
                        if check_prime(formula_out):
                            seq_len += 1
                        else:
                            mx = max(seq_len, mx)
                            if seq_len == mx:
                                coefficient_prod = a * b
                                msg(result_data, "New max sequence found! " + str(seq_len) + " with coefficient " + str(coefficient_prod) + " a " + str(a) + " b " + str(b))
                            break

            msg(result_data, "Result found: " + str(coefficient_prod))
            conclude(result_data, coefficient_prod, ALGO_BEGIN)

        solve() # -59231

    except Exception as ex:

        print('Exception: ' + str(ex))