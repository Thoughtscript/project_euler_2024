# https://projecteuler.net/problem=79
from lib import initialize, conclude, msg, correct_path_and_name
import time

if __name__ == '__main__':

    try:

        result_data = initialize(79, str(73162890), 0, 0, [])

        def init():
            stringData = ""
            fileHandler = open(correct_path_and_name('project_euler_79_input.txt'))
            for line in fileHandler:
                stringData += line.replace('"', '')

            result = stringData.split("\n")
            return result

        DATA = init()
        '''
        total = {}

        def calc_index_digits():
            for x in range(0, 3, 1):
                for y in range(0, len(DATA), 1):
                    total[DATA[y][x]] = DATA[y][x]

            print(total.values())

        calc_index_digits()
        '''
        '''
        {'3': '3', '6': '6', '1': '1', '7': '7', '2': '2', '8': '8'}
        {'1': '1', '8': '8', '9': '9', '2': '2', '6': '6', '3': '3'} 
        {'9': '9', '0': '0', '2': '2', '8': '8', '6': '6', '1': '1'} 
        ['3', '6', '1', '7', '2', '8', '9', '0']
        '''

        def make_key(arr):
            string_result = ""

            for x in range(0, len(arr), 1):
                string_result += str(arr[x])

            return string_result

        def permute(original_arr):
            transfer_arr = original_arr
            heaps_results = {}

            def swap(end, begin):
                original = transfer_arr[begin]
                transfer_arr[begin] = transfer_arr[end]
                transfer_arr[end] = original

            def heaps_algorithm(n):
                if n == 1: 
                    key = make_key(transfer_arr)
                    heaps_results[key] = key
                    return
            
                for i in range(0, n, 1):
                    heaps_algorithm(n-1)
                    v = 0
                    if n % 2 == 0:
                        v = i
                    swap(n-1, v)

            heaps_algorithm(len(original_arr))
            return heaps_results

        def deep_copy(arr):
            new_arr = []
            for x in range(0, len(arr), 1):
                new_arr.append(arr[x])
            return new_arr

        def make_nums(mx_len):
            total_vals = ['3', '6', '1', '7', '2', '8', '9', '0']
            result_set = []

            for x in range(0, mx_len - 8, 1):
                new_combo = ['3', '6', '1', '7', '2', '8', '9', '0']

                for y in range(0, 8, 1):
                    a = deep_copy(new_combo)
                    a.append(total_vals[y])
                    result_set.append(a)

            return result_set

        def string_split(num_as_str):
            response = []

            for x in range(0, len(num_as_str), 1):
                response.append(num_as_str[x])

            return response

        def check(num_as_str):
            msg(result_data, "Trying " + num_as_str)

            for x in range(0, len(DATA), 1):
                row_num_arr = string_split(DATA[x])
                last_idx = 0

                while len(row_num_arr) > 0:
                    current_digit = row_num_arr[0]
                    at_least_one_found = False

                    for y in range(last_idx, len(num_as_str), 1):
                        msg(result_data, "Matching " + current_digit + " " + num_as_str[y])
                        if current_digit == num_as_str[y]:
                             last_idx = y
                             row_num_arr.pop(0)
                             at_least_one_found = True
                             break
                        
                    if not at_least_one_found and len(row_num_arr) > 0:        
                        msg(result_data, num_as_str + " Failed")
                        return False
                   
            return True

        def solve(mx_num):
            ALGO_BEGIN = time.time()

            temp_total = [['3', '6', '1', '7', '2', '8', '9', '0']]
            for x in range(8, mx_num + 1, 1):
                x_nums = make_nums(x)
                for y in range(0, len(x_nums), 1):
                    temp_total.append(x_nums[y])

            permutation_total = []
            
            for x in range(0, len(temp_total), 1):
                heaps_list = list(permute(temp_total[x]).values())
                for y in range(0, len(heaps_list), 1):
                    permutation_total.append(heaps_list[y])
    
            for x in range(0, len(permutation_total), 1):
                if (check(permutation_total[x])):
                    msg(result_data, "Valid passcode found " + str(permutation_total[x]))
                    conclude(result_data, permutation_total[x], ALGO_BEGIN)
                    break

        solve(9) #73162890

        # So, I fucked this one up. See Lines 111-119 were fucked.
        ## Needed something like (and this is still wildly sub-optimal prob) log N (popping array) wrapping a Sliding Window Technique
        ## I was missing the correct boolean checks there

        # Also, I assumed it would be well above 8 length and so coded for like length 35 digits
        ## So, a lot of the Heap's > length 8 and make_nums stuff isn't needed since it's actualy length 8!

    except Exception as ex:

        print('Exception: ' + str(ex))