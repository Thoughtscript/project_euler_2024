# https://projecteuler.net/problem=53
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    try:

        result_data = initialize(53, 4075, 0, 0, [])

        def factorial(n):
            total = 1
            counter = n
            while(counter > 0):
                total *= counter
                counter -= 1
            return total

        def solve():
            ALGO_BEGIN = time.time()
            solution = 0

            for n in range(1, 101, 1):
                n_fact = factorial(n)
 
                for r in range(1, n + 1, 1):
                    r_fact = factorial(r)
                    n_minus_r_fact = factorial(n-r)
                    val = n_fact / (r_fact * n_minus_r_fact)
                    if (val > 1_000_000):
                        msg(result_data, "Value > 1_000_000 Found: [ n: " + str(n) + " r: " + str(r) + " ]")
                        solution += 1

            msg(result_data, "Solution found: " + str(solution))
            conclude(result_data, solution, ALGO_BEGIN)
            
        solve() # 4075

    except Exception as ex:
        print('Exception: ' + str(ex))