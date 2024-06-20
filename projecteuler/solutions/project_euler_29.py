# https://projecteuler.net/problem=29
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    result = initialize(29, 9183, 0, 0, [])

    try:

        def solve():
            ALGO_BEGIN = time.time()

            hm = {}

            for x in range(2, 101,1):
                for y in range(2, 101, 1):
                    val = pow(x, y)
                    hm[val] = True

            solution = len(hm.values())

            msg(result, str(solution) + " distinct values")
            conclude(result, solution, ALGO_BEGIN)

        solve() # 9183

    except Exception as ex:

        print('Exception: ' + str(ex))