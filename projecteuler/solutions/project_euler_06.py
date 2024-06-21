# https://projecteuler.net/problem=6
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    try:

        result_data = initialize(6, 25164150, 0, 0, [])

        def sum_of_squares(top):
            result = 0
            for x in range(1,top+1,1):
                result += pow(x, 2)

            msg(result_data, "sum_of_squares " + str(result))
            return result

        def square_of_sums(top):
            result = 0
            for x in range(1,top+1,1):
                result += x
            
            result = pow(result, 2)
            msg(result_data, "sum_of_squares " + str(result))
            return result
        
        def solve():
            ALGO_BEGIN = time.time()

            solution = square_of_sums(100) - sum_of_squares(100)
            
            conclude(result_data, solution, ALGO_BEGIN)

        solve() # 25164150

    except Exception as ex:
        print('Exception: ' + str(ex))