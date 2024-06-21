# https://projecteuler.net/problem=38
from lib import initialize, conclude, msg
import time

if __name__ == '__main__':

    try:

        result_data = initialize(38, 932718654, 0, 0, [])
        
        def is_pandigital(num):
            LEN = len(num)

            hm = {}
            for x in range(0, LEN, 1):
                N = int(num[x])

                if not (N >= 1 and N <= LEN):
                    return False

                V = hm.get(N)
                if V is None:
                    hm[N] = N
                else:
                    return False

            return True

        # The maximum upper bound is 987654321
        # A known lower bound is 918273645

        # Must be sequential multiples:
        # e.g. 1,2,3,4,...
        # Not 2,3,5,...
        # So, a shortcut / optimization is to break the inner loop if len > 9.
        def solve(MAX_NUM, MAX_MULTIPLE):
            ALGO_BEGIN = time.time()

            largest = 918273645

            for x in range(0, MAX_NUM, 1):
                temp = ''

                for y in range(1, MAX_MULTIPLE, 1):
                    temp += str(x * y)

                    if len(temp) > 9:
                        break
                    
                    if len(temp) == 9:
                        N = int(temp)
                        if N < largest:
                            continue

                        C = is_pandigital(temp)

                        if C:
                            msg(result_data, "New Pandigital multiple found! " + temp)
                            if N > largest:
                                largest = N

            conclude(result_data, largest, ALGO_BEGIN)

        solve(999_999, 1000) # 932718654
        
    except Exception as ex:

        print('Exception: ' + str(ex))