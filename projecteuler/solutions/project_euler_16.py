# https://projecteuler.net/problem=16
from lib import initialize, msg, conclude, sum_list
import time

if __name__ == '__main__':

    try:

        result_data = initialize(16, 1366, 0, 0, [])

        def solve():
            ALGO_BEGIN = time.time()
            
            num = pow(2, 1000)
            msg(result_data, "num: " + str(num))
            st = str(num)
            sm = sum_list(st)
            
            conclude(result_data, sm, ALGO_BEGIN)

        solve() # 1366

    except Exception as ex:
        print('Exception: ' + str(ex))