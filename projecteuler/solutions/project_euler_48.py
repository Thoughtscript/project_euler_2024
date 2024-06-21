# https://projecteuler.net/problem=48
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    try:

        result_data = initialize(48, 9110846700, 0, 0, [])

        def solve():
            ALGO_BEGIN = time.time()
            sum = 0

            for x in range(1, 1001, 1):
                sum = sum + pow(x, x)
            
            num_str = str(sum)
            msg(result_data, "Num: " + num_str)
            LEN = len(num_str)
            LAST_TEN = num_str[LEN-10:LEN]

            conclude(result_data, int(LAST_TEN), ALGO_BEGIN)

        solve() # 9110846700

    except Exception as ex:

        print('Exception: ' + str(ex))