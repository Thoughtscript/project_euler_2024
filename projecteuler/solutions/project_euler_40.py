# https://projecteuler.net/problem=40
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    result = initialize(40, 210, 0, 0, [])

    try:

        def solve():
            ALGO_BEGIN = time.time()

            # Only generate the decimal integers after the point
            decimal_str = ''

            for x in range(1,1000000,1):
               decimal_str = decimal_str + str(x)

            # Offset by one
            A = decimal_str[1-1]
            B = decimal_str[10-1]
            C = decimal_str[100-1]
            D = decimal_str[1000-1]
            E = decimal_str[10000-1]
            F = decimal_str[100000-1]
            G = decimal_str[1000000-1]

            msg(result, "A: " + str(A))
            msg(result, "B: " + str(B))
            msg(result, "C: " + str(C))
            msg(result, "D: " + str(D))
            msg(result, "E: " + str(E))
            msg(result, "F: " + str(F))
            msg(result, "G: " + str(G))

            solution = int(A) *int(B) * int(C) * int(D) * int(E) * int(F) * int(G)

            conclude(result, solution, ALGO_BEGIN)

        solve() # 210

    except Exception as ex:

        print('Exception: ' + str(ex))