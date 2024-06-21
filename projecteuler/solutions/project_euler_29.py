# https://projecteuler.net/problem=29
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    try:

        result_data = initialize(29, 9183, 0, 0, [])

        def solve():
            ALGO_BEGIN = time.time()

            hm = {}

            for x in range(2, 101,1):
                for y in range(2, 101, 1):
                    val = pow(x, y)
                    hm[val] = True

            solution = len(hm.values())

            msg(result_data, str(solution) + " distinct values")
            conclude(result_data, solution, ALGO_BEGIN)

        solve() # 9183

    except Exception as ex:

        print('Exception: ' + str(ex))