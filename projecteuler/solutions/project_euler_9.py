# https://projecteuler.net/problem=9
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    try:

        result_data = initialize(9, str([200,375,425]), 0, 0, [])

        def solve():
            ALGO_BEGIN = time.time()

            for a in range (0, 1001, 1):
                for b in range (0, 1001, 1):
                    for c in range (0, 1001, 1):
                        if (a + b + c == 1000 and a < b and b < c):
                            A = pow(a, 2) 
                            B = pow(b, 2)
                            C = pow(c, 2)
                            msg(result_data, "Triple: " + str(a) + " " + str(b) + " " + str(c))
                            if (A + B == C):
                                msg(result_data, "Triple found: " + str(a) + " " + str(b) + " " + str(c))
                                conclude(result_data, str([a, b, c]), ALGO_BEGIN)

            msg(result_data, "None found")
            
        solve() #  200 375 425

    except Exception as ex:
        print('Exception: ' + str(ex))