# https://projecteuler.net/problem=59
from lib import initialize, msg, conclude, correct_path_and_name
import time

if __name__ == '__main__':

    try:

        result_data = initialize(59, 129448, 0, 0, [])
        
        def init(file_name, sep):
            stringData = ""
            fileHandler = open(correct_path_and_name(file_name))
            for line in fileHandler:
                stringData += line.replace('"', '')

            result = stringData.split(sep)
            return result

        def solve():
            inputs = init('project_euler_59_input.txt',",")
            keys = []

            for a in range(97, 123, 1):
                for b in range(97, 123, 1):
                    for c in range(97, 123, 1):
                        let_a = chr(a)
                        let_b = chr(b)
                        let_c = chr(c)
                        key = let_a + let_b + let_c
                        keys.append(key)
            
            valid_strings = []
            special_chars = ["*", "{", "~" ]

            for k in range(0, len(keys), 1):
                key = keys[k]
                key_idx = 0
                result_str = ""
            
                for i in range(0, len(inputs), 1):
                    xor = ord(key[key_idx]) ^ int(inputs[i])
                    result_str += chr(xor)
                    key_idx += 1
                    if (key_idx >= 3):
                        key_idx = 0
                
                valid = True

                for j in range(0, len(result_str), 1):
                    for q in range(0, len(special_chars), 1):
                        if result_str[j] == special_chars[q]:
                            valid = False
                            break

                if valid:
                    valid_strings.append(result_str)
                
            # 'An extract taken from the introduction of one of Euler\'s most celebrated papers, "De summis serierum reciprocarum" [On the sums of series of reciprocals]: I have recently found, quite unexpectedly, an elegant expression for the entire sum of this series 1 + 1/4 + 1/9 + 1/16 + etc., which depends on the quadrature of the circle, so that if the true sum of this series is obtained, from it at once the quadrature of the circle follows. Namely, I have found that the sum of this series is a sixth part of the square of the perimeter of the circle whose diameter is 1; or by putting the sum of this series equal to s, it has the ratio sqrt(6) multiplied by s to 1 of the perimeter to the diameter. I will soon show that the sum of this series to be approximately 1.644934066842264364; and from multiplying this number by six, and then taking the square root, the number 3.141592653589793238 is indeed produced, which expresses the perimeter of a circle whose diameter is 1. Following again the same steps by which I had arrived at this sum, I have discovered that the sum of the series 1 + 1/16 + 1/81 + 1/256 + 1/625 + etc. also depends on the quadrature of the circle. Namely, the sum of this multiplied by 90 gives the biquadrate (fourth power) of the circumference of the perimeter of a circle whose diameter is 1. And by similar reasoning I have likewise been able to determine the sums of the subsequent series in which the exponents are even numbers.'
            return valid_strings

        def count_solution():
            ALGO_BEGIN = time.time()

            result = solve()[0]

            total = 0

            for x in range(0, len(result), 1):
                total += ord(result[x])

            msg(result_data, "ASCII total found: " + str(total))
            conclude(result_data, total, ALGO_BEGIN)
                
        count_solution() # 129448

    except Exception as ex:

        print('Exception: ' + str(ex))