# https://projecteuler.net/problem=81
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    try:

        result_data = initialize(81, 427337, 0, 0, [])

        def init():
            result_array = []
            fileHandler = open('data/project_euler_81_input.txt')
            for line in fileHandler:
                result_array.append(line.split(","))
            return result_array

        def make_temp_copy():
            result_array = [0] * 80

            for x in range(0, len(result_array), 1):
                result_array[x] = [0] * 80

            return result_array

        def solve():
            ALGO_BEGIN = time.time()

            orig_matrix = init()
            aux = make_temp_copy()

            # Top to Bottom
            # Left to Right
            for row in range(0, 80, 1):
                for col in range(0, 80, 1):
                    #Calc minimum path to each cell row, col
                    curr_cell = int(orig_matrix[row][col])

                    if col - 1 >= 0 and row - 1 >= 0:
                        l = curr_cell + aux[row][col-1]
                        u = curr_cell + aux[row-1][col]
                        aux[row][col] = min(u, l)
                   
                    if col - 1 >= 0 and not row - 1 >= 0:
                        aux[row][col] = curr_cell + aux[row][col-1]

                    if not col - 1 >= 0 and row - 1 >= 0:
                       aux[row][col] = curr_cell + aux[row-1][col]

                    if not col - 1 >= 0 and not row - 1 >= 0:
                         aux[row][col] = curr_cell

            conclude(result_data, aux[79][79], ALGO_BEGIN)

        solve() # 427337

    except Exception as ex:

        print('Exception: ' + str(ex))