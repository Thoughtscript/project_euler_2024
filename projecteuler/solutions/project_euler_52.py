# https://projecteuler.net/problem=52
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    try:

        result_data = initialize(52, 142857, 0, 0, [])

        def count_digits(num_str):
            hm = [0,0,0,0,0,0,0,0,0,0]

            for x in range(0, len(num_str), 1):
                key = int(num_str[x])
                hm[key] = hm[key] + 1
            
            return hm

        # Same count
        def same_count(a, b):
            for x in range(0, len(a), 1):
                if a[x] == b[x]:
                    continue
                else:
                    return False

            return True

        def permutated(arr):
            nums = len(arr)
            num_length = len(str(arr[0]))

            for y in range(0, num_length, 1):
                hm = {}

                for x in range(0, nums, 1):
                    num = str(arr[x])
                    check = hm.get(num[y])
                    if check is None:
                        hm[num[y]] = True
                    else:
                        return False

            return True

        def solve():
            ALGO_BEGIN = time.time()

            for x in range(1, 1000000, 1):
                hm_x = count_digits(str(x))
                temp_arr = []

                for y in range(1,7,1):
                    z = y * x

                    hm_z = count_digits(str(z))
                    if same_count(hm_x, hm_z):
                        temp_arr.append(z)
                        
                if len(temp_arr) == 6:
                    if permutated(temp_arr):
                        msg(result_data, "Number found: " + str(x))
                        conclude(result_data, x, ALGO_BEGIN)

            msg(result_data, "No number found!")
            
        solve() # 142857

    except Exception as ex:

        print('Exception: ' + str(ex))