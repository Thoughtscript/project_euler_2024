# https://projecteuler.net/problem=35
from lib import initialize, msg, conclude
import time

from data import primes_to_2_mil_map

if __name__ == '__main__':

    try:

        result_data = initialize(35, 55, 0, 0, [])

        PRIMES = primes_to_2_mil_map.primes

        def is_circular(num):
            rotation = str(num)
            LEN = len(rotation)
            count = 0

            while count < LEN:
                check = PRIMES.get(int(rotation))

                if check is None:
                    return False

                count += 1
                rotation = rotation[1:LEN] + rotation[0]

            msg(result_data, str(num) + " is circular")
            return True


        def solve():
            ALGO_BEGIN = time.time()

            count = 0

            for x in range(0, 999_999, 1):
                if is_circular(x):
                    count += 1

            msg(result_data, str(count) + " circular numbers found!")
            conclude(result_data, count, ALGO_BEGIN)

        solve()

    except Exception as ex:

        print('Exception: ' + str(ex))