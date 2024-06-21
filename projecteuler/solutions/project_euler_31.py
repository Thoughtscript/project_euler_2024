# https://projecteuler.net/problem=31
# had to look up how people approached integer partitions - several algorithms
# cleanest implementation I found as follows
# from https://leetcode.com/submissions/detail/755940600/
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    try:

        result_data = initialize(31, 73682, 0, 0, [])

        COIN_MAP = [1,2,5,10,20,50,100,200]

        # max total is max_n
        def prep_arr(max_n):
            lst = []
            for i in range(0, max_n + 1, 1):
                lst.append(0)

            # e.g. 10 - 10
            lst[0] = 1
            return lst

        def integer_partitions(max_n):
            lst = prep_arr(max_n)

            # general mathematical algorithm - integer partitions
            for i in range(0, len(COIN_MAP), 1):
                coin = COIN_MAP[i]

                for j in range(coin, max_n + 1, 1):
                    lst[j] = lst[j] + lst[j - coin]

            return lst[max_n]

        def solve(max_num):
            ALGO_BEGIN = time.time()
            
            results = integer_partitions(max_num)

            msg(result_data, "Number of solutions found: " + str(results))

            conclude(result_data, results, ALGO_BEGIN)
        
        solve(200) # 73682
            
    except Exception as ex:
        print('Exception: ' + str(ex))
