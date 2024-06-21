# https://projecteuler.net/problem=36
from lib import initialize, msg, conclude, sum_list
import time
import math

if __name__ == "__main__":

    try:

        result_data = initialize(36, 872187, 0, 0, [])

        def is_palindrome(num_str):
            LEN = len(num_str)
            HALF = int(math.floor(len(num_str) / 2))

            for x in range(0, HALF, 1):
                if num_str[x] == num_str[LEN - 1 - x]:
                   continue
                else:
                    return False
            
            return True

        def to_binary(num):
            return format(num, 'b')

        def solve():
            ALGO_BEGIN = time.time()

            result = []

            for x in range(0, 1000000, 1):
                num_str = str(x)
                A = is_palindrome(num_str)
                binary = to_binary(x)
                B = is_palindrome(binary)

                if A and B:
                    msg(result_data, "Double-base palindrome found: " + num_str)
                    result.append(x)

            sum = sum_list(result)

            conclude(result_data, sum, ALGO_BEGIN)
       
        solve()
      
    except Exception as ex:

        print("Exception: " + str(ex))