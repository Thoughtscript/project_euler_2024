# https://projecteuler.net/problem=14
from lib import initialize, conclude, msg
import time

if __name__ == '__main__':

    try:

        result_data = initialize(14, 837799, 0, 0, [])

        def sequence(num):
            result = []

            while True:
                result.append(num)

                if num == 1:
                    break

                if num % 2 == 0:
                    num /= 2
                else:
                    num = 3 * num + 1
                
            return result

        #sequence(13)
        #sequence(45)
        #sequence(20000)

        def solve(num):
            ALGO_BEGIN = time.time()

            mx = 0
            n = -1

            for x in range(1,num,1):
                s = sequence(x)
                if len(s) > mx:
                    mx = len(s)
                    n = x
                    msg(result_data, "New max found: " + str(s) + " number: " + str(x))
            
            msg(result_data, "Final number: " + str(n))

            conclude(result_data, n, ALGO_BEGIN)

        solve(999_999)

    except Exception as ex:
        print('Exception: ' + str(ex))