# https://projecteuler.net/problem=25
from lib import initialize, conclude, msg
import time

if __name__ == '__main__':

    try:

        result_data = initialize(25, 4782, 0, 0, [])

        def solve():
            ALGO_BEGIN = time.time()

            fib = [0,1]
            counter = 1

            while(len(str(fib[1])) < 1000):
                N = fib[0] + fib[1]
                fib[0] = fib[1]
                fib[1] = N
                counter += 1

            solution = str(fib[1])
            
            msg(result_data, "Found: " + str(counter) + " " + solution + " len " + str(len(solution)))
            conclude(result_data, counter, ALGO_BEGIN) 

        solve() # 4782

    except Exception as ex:

        print('Exception: ' + str(ex))