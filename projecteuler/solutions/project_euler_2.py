# https://projecteuler.net/problem=2
from lib import initialize, conclude, msg, sum_list
import time

if __name__ == '__main__':

    try:

        result_data = initialize(2, 4613732, 0, 0, [])

        def sum_up_to(lst, max_num):
            result = 0
            for i in range(0, len(lst), 1):
                if lst[i] % 2 == 0 and lst[i] <= max_num:
                    result += lst[i]
            
            return result

        # current < n
        # current_fib_num < max_num
        def innerFib(lst, n, current, max_num):
            if current < 2:
                lst.append (current)
            else:
                current_fib_num = lst[current - 2] + lst[current - 1]
                
                lst.append(current_fib_num)
                if current_fib_num >= max_num:
                    msg(result_data, "Max num " + str(max_num) + " surpassed at Fib. Num " + str(current) + " " + str(current_fib_num))
                    msg(result_data, lst)
                    return

            if current < n:
                current += 1
                innerFib(lst, n, current, max_num)

            else:
                #L = len(lst)

                # All generated numbers
                msg(result_data, lst)

                # Last number
                # msg(result_data, 'Last number: ' + str(lst[L - 1]))

                # Total numbers
                # msg(result_data, 'Total numbers: ' + str(L))

                # Nth number
                # msg(result_data, str(L) + '-th number is ' + str(lst[L - 1]))
                
                # Length of number in string representation
                # msg(result_data, 'Length of digit as string: ' + str(len(str(lst[L - 1]))))

        def fibonacci(n, max_num):
           msg(result_data, "Generating first " + str(n) + " Fib. Nums or all Fib. Nums up to " + str(max_num))

           result = []
           innerFib(result, n, 0, max_num)
           return sum_up_to(result, max_num)

        def solve():
            ALGO_BEGIN = time.time()

            solution = fibonacci(35, 4_000_000)

            conclude(result_data, solution, ALGO_BEGIN)
    
        solve() # 4613732

    except Exception as ex:

        print('Exception: ' + str(ex))