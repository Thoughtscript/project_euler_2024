# https://projecteuler.net/problem=55
from lib import initialize, msg, conclude, correct_path_and_name
import time
import math

if __name__ == '__main__':

    try:

        result_data = initialize(55, 249, 0, 0, [])

        def is_palindrome(num_str):
            LEN = len(num_str)
            HALF = int(math.floor(len(num_str) / 2))

            for x in range(0, HALF, 1):
                if num_str[x] == num_str[LEN - 1 - x]:
                   continue
                else:
                    return False
            
            return True

        def reverse_num_str(num_str):
            result = ''
            for x in range(len(num_str) - 1, -1, -1):
                result = result + num_str[x]

            return result

        # ------------- #

        # Lychrel numbers do not form palindromes when added to their reversed number.
        def solve(mx, iter):
            ALGO_BEGIN = time.time()
            result = 0
            num_str = '0'
            reversed_num_str = '0'
            val = 0
            val_str = '0'

            for x in range(0, 10000, 1):
                orig_num = str(x)
                found = False
                for y in range(0, iter, 1):
                    if y == 0:
                        num_str = orig_num
                    else:
                        num_str = val_str
                        
                    reversed_num_str = reverse_num_str(num_str)
                    val = int(num_str) + int(reversed_num_str)
                    val_str = str(val)
                    if is_palindrome(val_str):
                        found = True
                        break

                if not found:
                    msg(result_data, "Lychrel number found: " + orig_num)
                    result += 1
            
            msg(result_data, "There are " + str(result) + " Lychrel numbers below " + str(mx))
            conclude(result_data, result, ALGO_BEGIN)

        solve(10_000, 50) # 249


    except Exception as ex:

        print('Exception: ' + str(ex))