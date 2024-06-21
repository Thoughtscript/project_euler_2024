# https://projecteuler.net/problem=45
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    try:

        result_data = initialize(45, 1533776805, 0, 0, [])

        def make_triangle_nums(mx):
            result = {}
            for x in range(1, mx, 1):
                num = x * (x + 1) / 2
                result[num] = num

            return result

        def make_pentagonal_nums(mx):
            result = {}
            for x in range(1, mx, 1):
                num = x * (3 * x - 1) / 2
                result[num] = num

            return result

        def make_hexagonal_nums(mx):
            result = {}
            for x in range(1, mx, 1):
                num = x * (2 * x - 1)
                result[num] = num

            return result

        def solve(mx):
            ALGO_BEGIN = time.time()

            tri_map = make_triangle_nums(mx)
            pentagonal_map = make_pentagonal_nums(mx)
            hexagonal_map = make_hexagonal_nums(mx)

            TRI_VALS = list(tri_map.values())
            LEN_TRI_VALS = len(TRI_VALS)

            for x in range(1, LEN_TRI_VALS, 1):
                A = TRI_VALS[x]
                B = pentagonal_map.get(A)
                C = hexagonal_map.get(A)

                if B is None or C is None:
                    continue

                msg(result_data, "Number found: " + str(A))

                if A > 40755:
                    msg(result_data, "Next highest number found " + str(A))
                    conclude(result_data, A, ALGO_BEGIN)
            

        solve(100000) # 1533776805

    except Exception as ex:

        print('Exception: ' + str(ex))