# https://projecteuler.net/problem=15
# This is essentially: https://leetcode.com/problems/unique-paths/
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    try:

        result_data = initialize(15, 137846528820, 0, 0, [])

        def init(num):
            lattice = []

            # A 2 x 2 lattice should be represented as a 3 x 3 grid.
            # A 1 x 1 lattice should be represented as a 2 x 2 grid.
            for r in range(0,num+1,1):
                row = []
                for c in range(0,num+1,1):
                    row.append(0)

                lattice.append(row)

            return lattice

        def solve(lattice):
            ALGO_BEGIN = time.time()

            LEN = len(lattice)

            for r in range(0,LEN,1):
                for c in range(0,LEN,1):
                    if (r == 0):
                        lattice[r][c] = 1
                    else:
                        if (r > 0):
                            lattice[r][c] += lattice[r-1][c]
                        if (c > 0):
                            lattice[r][c] += lattice[r][c-1]

            conclude(result_data, lattice[LEN - 1][LEN - 1], ALGO_BEGIN)
            
        solve(init(20))

        # 1
        # [
        #   [1, 1], 
        #   [1, 2]
        # ]

        # 2
        # [
        #   [1, 1, 1], 
        #   [1, 2, 3], 
        #   [1, 3, 6]
        # ]

    except Exception as ex:

        print('Exception: ' + str(ex))