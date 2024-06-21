# https://projecteuler.net/problem=92
from lib import initialize, conclude
import time

if __name__ == '__main__':

    try:

        result_data = initialize(92, 8581146, 0, 0, [])

        # cache these for way faster performance
        ## transitive checking
        hm1 = {1:1}
        hm89 = {89:89}

        def digit_square_and_sum(num):
            num_as_str = str(num)
            result = 0

            for x in range(0, len(num_as_str), 1):
                result += pow(int(num_as_str[x]), 2)

            return result
        
        def loop(currNum):
            current_digit_sum = digit_square_and_sum(currNum)
            temp = []
            temp.append(current_digit_sum)
            is_1_loop = not hm1.get(current_digit_sum) is None
            is_89_loop = not hm89.get(current_digit_sum) is None
     
            while not (is_1_loop or is_89_loop):
                current_digit_sum = digit_square_and_sum(current_digit_sum)
                temp.append(current_digit_sum)
                is_1_loop = not hm1.get(current_digit_sum) is None
                is_89_loop = not hm89.get(current_digit_sum) is None

            if not hm1.get(current_digit_sum) is None:
                for x in range(0, len(temp), 1):
                    hm1[temp[x]] = temp[x]
                return False
            
            if not hm89.get(current_digit_sum) is None:
                for x in range(0, len(temp), 1):
                    hm89[temp[x]] = temp[x]
                return True

        def solve():
            ALGO_BEGIN = time.time()

            count_nums = 0

            for x in range(1, 10_000_001, 1):
                if loop(x):
                    count_nums+=1

            conclude(result_data, count_nums, ALGO_BEGIN)

        solve() # 8581146

    except Exception as ex:

        print('Exception: ' + str(ex))