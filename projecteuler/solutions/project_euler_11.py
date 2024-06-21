# https://projecteuler.net/problem=11
from lib import initialize, msg, conclude, load_json_file, correct_path_and_name
import time

if __name__ == '__main__':

    try:

        result_data = initialize(11, 70600674, 0, 0, [])

        def left_right(grid, r, c):
            msg(result_data, "Left-Right for: " + str(grid[r][c]))
            min = c - 3
            max = c + 3

            while min < 0:
                min += 1

            while max >= len(grid[r]):
                max -= 1

            product = int(grid[r][min]) * int(grid[r][min+1]) * int(grid[r][min+2]) * int(grid[r][min+3])
            counter = min + 4
            mx = product

            arr = [grid[r][min], grid[r][min+1], grid[r][min+2], grid[r][min+3]]

            while (counter <= max):
                if int(grid[r][counter-3]) > 0:
                    product = product / int(grid[r][counter-3])
                product = product * int(grid[r][counter])

                arr.pop(0)
                arr.append(grid[r][counter])

                counter = counter + 1
                if mx < product:
                    mx = product

            return mx

        def up_down(grid, r, c):
            msg(result_data, "Up-Down for: " + str(grid[r][c]))
            min = r - 3
            max = r + 3

            while min < 0:
                min += 1

            while max >= len(grid):
                max -= 1

            product = int(grid[min][c]) * int(grid[min+1][c]) * int(grid[min+2][c]) * int(grid[min+3][c])
            counter = min+4
            mx = product

            arr = [grid[min][c], grid[min+1][c], grid[min+2][c], grid[min+3][c]]

            while (counter <= max):
                if int(grid[counter-3][c]) > 0:
                    product = product / int(grid[counter-3][c])
                product = product * int(grid[counter][c])

                arr.pop(0)
                arr.append(grid[counter][c])

                counter = counter + 1
                if mx < product:
                    mx = product

            return mx

        # (0,0)
        #  (1,1)
        #   (2,2)
        #    (3,3)
        #     (4,4)
        #      (5,5)
        #       (6,6)

        #       (0,6)
        #      (1,5)
        #     (2,4)
        #    (3,3)
        #   (4,2)
        #  (5,1)
        # (6,0)

        # ===================

        # (0,1)
        #  (1,2)
        #   (2,3)
        #    (3,4)
        #     (4,5)
        #      (5,6)
        #       (6,7)

        #       (0,7)
        #      (1,6)
        #     (2,5)
        #    (3,4)
        #   (4,3)
        #  (5,2)
        # (6,1)

        def diags(grid, r, c):
            mx = 0
            msg(result_data, "Diags for: " + str(grid[r][c]))
            r_min = r - 3
            r_max = r + 3
            c_min = c - 3
            c_max = c + 3

            while r_min < 0 or c_min < 0:
                r_min += 1
                c_min += 1

            while r_max >= len(grid) or c_max >= len(grid[r]):
                r_max -= 1
                c_max -= 1

            if not (r_max - r_min < 3 or c_max - c_min < 3):
                product = int(grid[r_min][c_min]) * int(grid[r_min+1][c_min+1]) * int(grid[r_min+2][c_min+2]) * int(grid[r_min+3][c_min+3])
                r_counter = r_min+4
                c_counter = c_min+4

                arr = [grid[r_min][c_min], grid[r_min+1][c_min+1],
                       grid[r_min+2][c_min+2], grid[r_min+3][c_min+3]]

                while (r_counter <= r_max and c_counter <= c_max):
                    if int(grid[r_counter-3][c_counter-3]) > 0:
                        product = product / int(grid[r_counter-3][c_counter-3])
                    product = product * int(grid[r_counter][c_counter])

                    arr.pop(0)
                    arr.append(grid[r_counter][c_counter])

                    r_counter += 1
                    c_counter += 1
                    if mx < product:
                        mx = product

            r_min = r - 3
            r_max = r + 3
            c_min = c + 3
            c_max = c - 3

            while r_min < 0 or c_min >= len(grid[r]):
                r_min += 1
                c_min -= 1

            while r_max >= len(grid) or c_max < 0:
                r_max -= 1
                c_max += 1

            if not (r_max - r_min < 3 or c_min - c_max < 3):
                product = int(grid[r_min][c_min]) * int(grid[r_min+1][c_min-1]) * int(grid[r_min+2][c_min-2]) * int(grid[r_min+3][c_min-3])
                r_counter = r_min+4
                c_counter = c_min-4

                if mx < product:
                    mx = product

                arr = [grid[r_min][c_min], grid[r_min+1][c_min-1], grid[r_min+2][c_min-2], grid[r_min+3][c_min-3]]

                while (r_counter <= r_max and c_counter >= c_max):
                    if int(grid[r_counter-3][c_counter+3]) > 0:
                        product = product / int(grid[r_counter-3][c_counter+3])
                    product = product * int(grid[r_counter][c_counter])

                    arr.pop(0)
                    arr.append(grid[r_counter][c_counter])

                    r_counter = r_counter + 1
                    c_counter = c_counter - 1
                    if mx < product:
                        mx = product

            return mx

        def solve(grid):
            ALGO_BEGIN = time.time()

            mx = 0
            for r in range(0, len(grid), 1):
                for c in range(0, len(grid[0]), 1):
                    msg(result_data, "Row: " + str(r) + " Col: " + str(c) + " Val: " + str(grid[r][c]))

                    A = left_right(grid, r, c)
                    B = up_down(grid, r, c)
                    C = diags(grid, r, c)

                    msg(result_data, "Left-Right: " + str(A) + " Up-Down: " + str(B) + " Diags: " + str(C))
                    mx = max(A, B, C, mx)

            conclude(result_data, mx, ALGO_BEGIN)

        solve(load_json_file(correct_path_and_name('project_euler_11_data')))

    except Exception as ex:

        print('Exception: ' + str(ex))
