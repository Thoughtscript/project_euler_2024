# https://projecteuler.net/problem=18
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    try:

        result_data = initialize(18, 1074, 0, 0, [])

        # Start from bottom up:
        # DATA[r-1][c] += Math.max(DATA[r][c], DATA[r][c+1])

        DATA = [
            [75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
            [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
        ]

        def check_below(r, c):
            next_row = r + 1
            same_col = c
            next_col = c + 1
            DATA[r][c] =  DATA[r][c] + max(DATA[next_row][same_col], DATA[next_row][next_col])

        def solve():
            ALGO_BEGIN = time.time()

            for r in range(len(DATA) - 2, -1, -1):
                for c in range(0, len(DATA[r]), 1):
                    check_below(r, c)

            conclude(result_data, DATA[0][0], ALGO_BEGIN)
     
        solve() # 1074

        # [
        #   [1074], 
        #   [995, 999], 
        #   [818, 900, 935], 
        #   [704, 801, 853, 792], 
        #   [686, 640, 766, 731, 782], 
        #   [666, 614, 636, 684, 660, 717], 
        #   [647, 501, 613, 609, 533, 657, 683], 
        #   [559, 499, 479, 536, 514, 526, 594, 616], 
        #   [460, 434, 419, 475, 508, 470, 510, 524, 487], 
        #   [419, 365, 393, 387, 419, 425, 430, 376, 454, 322], 
        #   [378, 317, 231, 321, 354, 372, 393, 354, 360, 293, 247], 
        #   [325, 246, 187, 178, 256, 329, 273, 302, 263, 242, 193, 233], 
        #   [255, 235, 154, 150, 140, 179, 256, 209, 224, 172, 174, 176, 148], 
        #   [125, 164, 102, 95, 112, 123, 165, 128, 166, 109, 122, 147, 100, 54], 
        #   [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
        # ]
        

    except Exception as ex:

        print('Exception: ' + str(ex))