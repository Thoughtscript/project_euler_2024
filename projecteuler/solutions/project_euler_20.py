# https://projecteuler.net/problem=20
from lib import initialize, sum_list, conclude
import time

if __name__ == '__main__':

    try:

        result_data = initialize(20, 648, 0, 0, [])

        def py_factor(num):
            total = 1

            for x in range(num, 0, -1):
                total *= x

            return total

        # py_factor(100) # 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

        def solve():
            ALGO_BEGIN = time.time()

            num_str = str(py_factor(100))
            solution = sum_list(num_str)

            conclude(result_data, solution, ALGO_BEGIN) 
            
        solve() # 648
    
    except Exception as ex:

        print('Exception: ' + str(ex))