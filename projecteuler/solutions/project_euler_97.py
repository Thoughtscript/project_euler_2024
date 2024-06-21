# https://projecteuler.net/problem=97
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    try:

        result_data = initialize(97, 8739992577, 0, 0, [])

        def solve():
            ALGO_BEGIN = time.time()

            num = 28433 * pow(2, 7830457) + 1
            str_num = str(num)
            L = len(str_num)
            if not L == 2357207: # Given in problem
                raise Exception("Incorrect answer!")
            
            last_ten = str_num[-10:]
            if not len(last_ten) == 10:
                raise Exception("Incorrect answer!")
            
            conclude(result_data, int(last_ten), ALGO_BEGIN)

        solve() # 8739992577

    except Exception as ex:

        print('Exception: ' + str(ex))