# https://projecteuler.net/problem=1
from lib import initialize, conclude, sum_list
import time

if __name__ == '__main__':

    try:

        result_data = initialize(1, 233168, 0, 0, [])

        def solve(n):
            ALGO_BEGIN = time.time()

            result = []

            for i in range(0, n, 1):
                if i % 3 == 0 or i % 5 == 0:
                    result.append(i)

            solution = sum_list(result)
            conclude(result_data, solution, ALGO_BEGIN)
    
        solve(1000) # 233168

    except Exception as ex:

        print('Exception: ' + str(ex))