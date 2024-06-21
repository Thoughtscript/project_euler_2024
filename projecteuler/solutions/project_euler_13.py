# https://projecteuler.net/problem=13
from lib import initialize, conclude, load_json_file, sum_list
import time

if __name__ == '__main__':

    try:

        result_data = initialize(13, 5537376230390876637302048746832985971773659831892672, 0, 0, [])

        def solve(lst):
            ALGO_BEGIN = time.time()

            sum = sum_list(lst)

            conclude(result_data, sum, ALGO_BEGIN)

        solve(load_json_file('data/project_euler_13_data')) # 5537376230390876637302048746832985971773659831892672
        
    except Exception as ex:

        print('Exception: ' + str(ex))