# https://projecteuler.net/problem=96
# All solutions are gauranteed to be unique
from lib import initialize, conclude, msg, correct_path_and_name
import time

if __name__ == '__main__':

    try:
        result_data = initialize(96, 24702, 0, 0, [])

        def init():
            file_handler = open(correct_path_and_name('project_euler_96_input.txt'))
            result_arr = []
            grid = []

            for line in file_handler:
                if line[0] == 'G':
                    if (len(grid) > 0):
                        result_arr.append(grid)
                        grid = []
                    continue

                if len(line) == 0:
                    continue

                cleaned = list(line.replace('\n', ''))
                row = []
                for i in range(0, len(cleaned), 1):
                    row.append(int(cleaned[i]))
                grid.append(row)

            result_arr.append(grid)
            return result_arr

        # Create new deep copy
        def concat(a, b):
            result = []

            for x in range(0, len(a), 1):
                result.append(a[x])

            for y in range(0, len(b), 1):
                result.append(b[y])

            return result

        def indexOf(arr, val):
            try:
                for i in range(0, len(arr), 1):
                    if arr[i] == val:
                        return i
                return -1

            except ValueError as ex:
                return -1

        def findNextEmpty(sudoku):
            for i in range(0, len(sudoku), 1):
                for j in range(0, len(sudoku[i]), 1):
                    if sudoku[i][j] == 0:
                        return [i, j]

            # If board is full returns false
            return False

        def getGrids(sudoku):
            return [
                [
                    sudoku[0][0],
                    sudoku[0][1],
                    sudoku[0][2],
                    sudoku[1][0],
                    sudoku[1][1],
                    sudoku[1][2],
                    sudoku[2][0],
                    sudoku[2][1],
                    sudoku[2][2],
                ],
                [
                    sudoku[0][3],
                    sudoku[0][4],
                    sudoku[0][5],
                    sudoku[1][3],
                    sudoku[1][4],
                    sudoku[1][5],
                    sudoku[2][3],
                    sudoku[2][4],
                    sudoku[2][5],
                ],
                [
                    sudoku[0][6],
                    sudoku[0][7],
                    sudoku[0][8],
                    sudoku[1][6],
                    sudoku[1][7],
                    sudoku[1][8],
                    sudoku[2][6],
                    sudoku[2][7],
                    sudoku[2][8],
                ],
                [
                    sudoku[3][0],
                    sudoku[3][1],
                    sudoku[3][2],
                    sudoku[4][0],
                    sudoku[4][1],
                    sudoku[4][2],
                    sudoku[5][0],
                    sudoku[5][1],
                    sudoku[5][2],
                ],
                [
                    sudoku[3][3],
                    sudoku[3][4],
                    sudoku[3][5],
                    sudoku[4][3],
                    sudoku[4][4],
                    sudoku[4][5],
                    sudoku[5][3],
                    sudoku[5][4],
                    sudoku[5][5],
                ],
                [
                    sudoku[3][6],
                    sudoku[3][7],
                    sudoku[3][8],
                    sudoku[4][6],
                    sudoku[4][7],
                    sudoku[4][8],
                    sudoku[5][6],
                    sudoku[5][7],
                    sudoku[5][8],
                ],
                [
                    sudoku[6][0],
                    sudoku[6][1],
                    sudoku[6][2],
                    sudoku[7][0],
                    sudoku[7][1],
                    sudoku[7][2],
                    sudoku[8][0],
                    sudoku[8][1],
                    sudoku[8][2],
                ],
                [
                    sudoku[6][3],
                    sudoku[6][4],
                    sudoku[6][5],
                    sudoku[7][3],
                    sudoku[7][4],
                    sudoku[7][5],
                    sudoku[8][3],
                    sudoku[8][4],
                    sudoku[8][5],
                ],
                [
                    sudoku[6][6],
                    sudoku[6][7],
                    sudoku[6][8],
                    sudoku[7][6],
                    sudoku[7][7],
                    sudoku[7][8],
                    sudoku[8][6],
                    sudoku[8][7],
                    sudoku[8][8],
                ]
            ]

        def col(sudoku, c):
            return [
                sudoku[0][c],
                sudoku[1][c],
                sudoku[2][c],
                sudoku[3][c],
                sudoku[4][c],
                sudoku[5][c],
                sudoku[6][c],
                sudoku[7][c],
                sudoku[8][c],
            ]

        def gridFromRowCol(r, c, sudoku):
            grids = getGrids(sudoku)

            if r < 3 and c < 3:
                return grids[0]
            if r < 3 and c >= 3 and c < 6:
                return grids[1]
            if r < 3 and c >= 6:
                return grids[2]
            if r >= 3 and r < 6 and c < 3:
                return grids[3]
            if r >= 3 and r < 6 and c >= 3 and c < 6:
                return grids[4]
            if r >= 3 and r < 6 and c >= 6:
                return grids[5]
            if r >= 6 and c < 3:
                return grids[6]
            if r >= 6 and c >= 3 and c < 6:
                return grids[7]
            if r >= 6 and c >= 6:
                return grids[8]

        def spotCheck(r, c, sudoku):
            used = []
            avail = []

            row = sudoku[r]
            for i in range(0, len(row), 1):
                if indexOf(used, row[i]) == -1:
                    used.append(row[i])

            cl = col(sudoku, c)
            for i in range(0, len(row), 1):
                if indexOf(used, cl[i]) == -1:
                    used.append(cl[i])

            grid = gridFromRowCol(r, c, sudoku)
            for i in range(0, len(row), 1):
                if indexOf(used, grid[i]) == -1:
                    used.append(grid[i])

            for i in range(1, 10, 1):
                if indexOf(used, i) == -1:
                    avail.append(i)

            return [avail, used]

        def solve(puzzle):
            # Return the solved puzzle as a 2d array of 9 x 9
            # Find next empty
            em = findNextEmpty(puzzle)
            if not em == False:
                r = em[0]
                c = em[1]
                sc = spotCheck(r, c, puzzle)
                avail = sc[0]

                if len(avail) == 0:
                    return [False, concat(puzzle, [])]

                for i in range(0, len(avail), 1):
                    puzzle[r][c] = avail[i]

                    s = solve(puzzle)
                    if s[0] == True:
                        return [True, concat(puzzle, [])]
                    puzzle[r][c] = 0

                return [False, concat(puzzle, [])]
            return [True, concat(puzzle, [])]

        def sudoku_solver(puzzle):
            result = solve(puzzle)
            if result[0] == True:
                return result[1]
            return

# ------------------------------------- #

        def solve_p_e():
            ALGO_BEGIN = time.time()

            data = init()
            results = []

            for x in range(0, len(data), 1):
                solved = solve(data[x])
                if solved[0] == True:
                    results.append(solved[1])
                else:
                    raise Exception("Invalid solution found!")

            if len(results) < 50:
                raise Exception("Fewer than 50 solutions found!")

            sum = 0
            for x in range(0, len(results), 1):
                numStr = str(results[x][0][0]) + str(results[x][0][1]) + str(results[x][0][2])
                msg(result_data, numStr)
                sum += int(numStr)

            msg(result_data, "Final sum: " + str(sum))
            conclude(result_data, sum, ALGO_BEGIN)

        solve_p_e() # 24702

    except Exception as ex:

        print('Exception: ' + str(ex))
