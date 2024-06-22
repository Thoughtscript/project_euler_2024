# https://projecteuler.net/problem=73
from lib import initialize, conclude
import time
from decimal import *

if __name__ == '__main__':

    try:

        result_data = initialize(73, 7295372, 0, 0, [])

        # Assume n < d
        def reduced_proper_fraction(n, d):
            k = 2

            if n == 1:
                return [n, d, str(n) + "/" + str(d)]

            while k <= n:
                if n % k == 0 and d % k == 0:
                    n = n // k
                    d = d // k
                else:
                    k += 1
                
            return [n, d, str(n) + "/" + str(d)]

        # reduced_proper_fraction(92, 100)
        # reduced_proper_fraction(2, 10)
        # reduced_proper_fraction(400, 12000)
        # reduced_proper_fraction(38, 112)
             
        def solve(denom):
            ALGO_BEGIN = time.time()

            hm = {}
            ONE_THIRD = Decimal(1)/Decimal(3)
            ONE_HALF = Decimal(1)/Decimal(2)

            # 1/3 to 1/2
            # d <= 12,000 not d == 12,000!
            # 4000/12000 to 6000/12000

            for d in range(1, denom + 1, 1):
                for n in range(1, denom + 1, 1):

                    # Will always get bigger -> break.
                    if n > d:
                        break

                    DEC = Decimal(n) / Decimal(d)

                    if DEC <= ONE_THIRD:
                        continue

                    # Will always get bigger -> break.
                    if DEC >= ONE_HALF:
                        break

                    rpf = reduced_proper_fraction(n, d)
                    S = rpf[2]

                    if hm.get(S) is None:
                        hm[S] = [S]
                    else:
                        hm[S].append(S)

            conclude(result_data, len(hm), ALGO_BEGIN)

        solve(12_000) # 7295372

    except Exception as ex:

        print('Exception: ' + str(ex))