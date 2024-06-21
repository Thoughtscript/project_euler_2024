# https://projecteuler.net/problem=56
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    try:

        result_data = initialize(56, 972, 0, 0, [])

        def digit_sum(num_str):
            sum = 0

            for x in range(0, len(num_str), 1):
                sum += int(num_str[x])

            return sum

        def solve():
            ALGO_BEGIN = time.time()

            mx_num = 0

            for a in range(0, 100, 1):
                for b in range(0, 100, 1):
                    num = pow(a, b)
                    num_str = str(num)
                    digit_sum_score =  digit_sum(num_str)
                    if mx_num < digit_sum_score:
                        mx_num = max(mx_num, digit_sum_score)
                        msg(result_data, "New largest digit sum found: " + str(digit_sum_score) + " for num " + num_str)
            
            conclude(result_data, mx_num, ALGO_BEGIN)

        solve() # New largest digit sum found: 972 for num 3848960788934848611927795802824596789608451156087366034658627953530148126008534258032267383768627487094610968554286692697374726725853195657679460590239636893953692985541958490801973870359499

    except Exception as ex:

        print('Exception: ' + str(ex))