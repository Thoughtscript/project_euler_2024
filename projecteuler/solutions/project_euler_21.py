# https://projecteuler.net/problem=21
from lib import initialize, conclude, msg
import time

if __name__ == '__main__':

    try:

        result_data = initialize(21, 31626, 0, 0, [])

        def d(n):
            divisors = []

            for x in range(1, n, 1):
                if n % x == 0:
                    divisors.append(x)

            sum = 0

            for x in range(0, len(divisors), 1):
                sum += divisors[x]

            return sum

        def generate(mx):
            hm = {}

            for x in range(1, mx+1, 1):
                hm[x] = d(x)

            return hm

        def amicable_pair(x, y):
            if x == d(y) and y == d(x) and not x == y and not y == x:
                return [True, x + y]
            return [False, 0]

        def solve(mx):
            ALGO_BEGIN = time.time()
            hm = generate(mx)

            keys = hm.keys()
            found = {}
            sum = 0

            for x in range(0, len(keys), 1):
                for y in range(0, len(keys), 1):
                    if (x == hm.get(y) and y == hm.get(x) and not x == y and not y == x):
                        if found.get(str(x) + str(y)) is None:                        
                            sum += x + y
                            msg(result_data, "Amicable Pair found: " + str(x) + " " + str(y) + " sum " + str(sum))
                            found[str(x) + str(y)] = True
                            found[str(y) + str(x)] = True
                        else:
                            msg(result_data, "Pair already found")

            conclude(result_data, sum, ALGO_BEGIN)

        solve(10_000)

        # Amicable Pair found: 220 284
        # Pair already found
        # Amicable Pair found: 1184 1210
        # Pair already found
        # Amicable Pair found: 2620 2924
        # Pair already found
        # Amicable Pair found: 5020 5564
        # Pair already found
        # Amicable Pair found: 6232 6368
        # Pair already found
        # 31626

    except Exception as ex:

        print('Exception: ' + str(ex))