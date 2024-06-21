# https://projecteuler.net/problem=4
from lib import initialize, conclude, msg
import time

if __name__ == '__main__':

    try:
        result_data = initialize(4, 906609, 0, 0, [])

        # Minimum = 100 x 100
        # 10000
        # Maximum = 999 x 999
        # 998001
        #
        # The min and max numbers have a length difference of one.
        #
        # There are 9 x 9 x 9 left-side values that can be generated 
        # for length 6 strings that are reflected into palindromes.
        # There are the same for 5 length values.

        def make_palindromes():
            result = []
            for x in range(0,10,1):
                for y in range(0,10,1):
                    for z in range(0,10,1):

                        a = str(x) + str(y) + str(z) + str(z) + str(y) + str(x)
                        if int(a) < 998002 and int(a) > 9999:
                            if not x == 0:
                                result.append(int(a))
                                msg(result_data, str(int(a)))

                        b = str(x) + str(y) + str(z) + str(y) + str(x)
                        if int(b) > 9999:
                            result.append(int(b))
                            msg(result_data, str(int(b)))

            result.sort()
            return result

        def solve():
            ALGO_BEGIN = time.time()

            palindromes = make_palindromes()
            
            mx = 0
            for n in palindromes:
                for x in range(100,1000,1):
                    if n % x == 0:
                        a = str(x)
                        b = str(n // x)
                        if len(a) == 3 and len(b) == 3:
                            if n > mx:
                                msg(result_data, "Numbers found: " + a + " " + b + " cleanly divide " + str(n))
                                mx = n

            conclude(result_data, mx, ALGO_BEGIN)
            return mx

        solve() # 906609

    except Exception as ex:

        print('Exception: ' + str(ex))