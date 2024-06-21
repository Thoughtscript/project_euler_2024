# https://projecteuler.net/problem=23
from lib import initialize, conclude, msg
import time

if __name__ == '__main__':

    try:

        result_data = initialize(23, 4179871, 0, 0, [])

        def proper_divisors_of(num):
            divisors = []

            for x in range(1, num, 1):
                if num % x == 0:
                    divisors.append(x)

            return divisors

        def sum_array(arr):
            result = 0

            for x in range(0, len(arr), 1):
                result += arr[x]

            return result

        # If False and equal it's neither abundant nor deficient. It's perfect.
        # If False, it's not deficient
        def is_abundant(num):
            divisors = proper_divisors_of(num)
            sum = sum_array(divisors)

            if sum > num:
                return True

            # if sum == num:
                # print("Neither abundant nor deficient. It's perfect.")

            return False

        # ------------------------------------------------ #

        def find_all_abundant():
            abundant_numbers = []

            for x in range(1, 28123 + 1, 1):
                if is_abundant(x):
                    abundant_numbers.append(x)

            return abundant_numbers

        def generate_answer_space():
            abundant_numbers = find_all_abundant()
            LEN = len(abundant_numbers)
            hm = {}

            for i in range(0, LEN, 1):
                I = abundant_numbers[i]
                for j in range(0, LEN, 1):
                    J = abundant_numbers[j]

                    if I + J > 28123:
                        break

                    hm[I + J] = True

            return hm

        def solve():
            ALGO_BEGIN = time.time()

            not_two_abundant_nums = []
            hm = generate_answer_space()

            # All numbers above 28123 are known to be 
            # writeable as the sum of two abundant numbers.
            for x in range(1, 28124, 1):
                n = hm.get(x)
                if n is None:
                    msg(result_data, str(x) + " cannot be expressed as the sum of two abundant numbers.")
                    not_two_abundant_nums.append(x)

            msg(result_data, not_two_abundant_nums)
            result = sum_array(not_two_abundant_nums)
            conclude(result_data, result, ALGO_BEGIN)

        solve() # 4179871

    except Exception as ex:

        print('Exception: ' + str(ex))
