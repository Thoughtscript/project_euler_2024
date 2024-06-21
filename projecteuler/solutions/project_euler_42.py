# https://projecteuler.net/problem=42
from lib import initialize, msg, conclude, correct_path_and_name
import time

if __name__ == '__main__':

    try:

        result_data = initialize(42, 162, 0, 0, [])

        LETTERS = {
            "A":1,
            "B":2,
            "C":3,
            "D":4,
            "E":5,
            "F":6,
            "G":7,
            "H":8,
            "I":9,
            "J":10,
            "K":11,
            "L":12,
            "M":13,
            "N":14,
            "O":15,
            "P":16,
            "Q":17,
            "R":18,
            "S":19,
            "T":20,
            "U":21,
            "V":22,
            "W":23,
            "X":24,
            "Y":25,           
            "Z":26
        }
        
        def make_triangle_nums():
            result = {}
            for x in range(1, 10000, 1):
                num = x * (x + 1) / 2
                result[num] = num

            return result

        def init():
            stringData = ""
            fileHandler = open(correct_path_and_name('project_euler_42_input.txt'))
            for line in fileHandler:
                stringData += line.replace('"', '')

            result = stringData.split(",")
            return result

        DATA = init()
        TRIANGLE_NUMS = make_triangle_nums()

        def solve():
            ALGO_BEGIN = time.time()

            triangle_words = 0

            for x in range(0, len(DATA), 1):
                word = DATA[x]
                sum = 0

                for y in range(0, len(word), 1):
                    sum = sum + LETTERS[word[y]]
                
                if TRIANGLE_NUMS.get(sum):
                    triangle_words = triangle_words + 1
                    msg(result_data, "Triangle Word found: " + word)

            msg(result_data, "Total Triangle Words found: " + str(triangle_words))
            conclude(result_data, triangle_words, ALGO_BEGIN)

        solve() # 162

    except Exception as ex:

        print('Exception: ' + str(ex))