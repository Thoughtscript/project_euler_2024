# https://projecteuler.net/problem=89
# From my solution: https://www.codewars.com/kata/51b66044bce5799a7f000003/train/javascript
from lib import initialize, msg, conclude, correct_path_and_name
import time

if __name__ == '__main__':

    try:

        result_data = initialize(89, 743, 0, 0, [])

        def to_roman(num):
            current = int(num)
            r = ""

            while current > 0:

                if current >= 1000:
                    r += "M"
                    current -= 1000
                    continue

                if current >= 100:
                    if current >= 900:
                        r += "CM"
                        current -= 900
                        continue

                    if current >= 500:
                        r += "D"
                        current -= 500
                        continue

                    if current >= 400:
                        r += "CD"
                        current -= 400
                        continue

                    r += "C"
                    current -= 100
                    continue

                if current >= 10:
                    if current >= 90:
                        r += "XC"
                        current -= 90
                        continue
    
                    if current >= 50:
                        r += "L"
                        current -= 50
                        continue
                    
                    if current >= 40:
                        r += "XL"
                        current -= 40
                        continue
                    
                    if current >= 10:
                        r += "X"
                        current -= 10
                        continue

                    continue

                if current < 10:
                    if current >= 9:
                        r += "IX"
                        current -= 9
                        continue
                
                    if current >= 5:
                        r += "V"
                        current -= 5
                        continue
                
                    if current >= 4:
                        r += "IV"
                        current -= 4
                        continue
                
                    if current >= 1:
                        r += "I"
                        current -= 1
                        continue
                
                    continue

            return r

        def from_roman(s):

            NUMS = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
            }

            total = 0
            x = 0

            # Range is immutable in a for loop.
            # Must use while loop here.
            while (x < len(s)):
                C = s[x]
                N = NUMS.get(C)

                if x < len(s) - 1:
                    CC = s[x + 1]

                    if C == 'I' and CC == 'V':
                        N = 4
                        x += 1
            
                    if C == 'I' and CC == 'X':
                        N = 9
                        x += 1
                
                    if C == 'X' and CC == 'L':
                        N = 40
                        x += 1
                
                    if C == 'X' and CC == 'C':
                        N = 90
                        x += 1
                
                    if C == 'C' and CC == 'D':
                        N = 400
                        x += 1
                
                    if C == 'C' and CC == 'M':
                        N = 900
                        x += 1

                total += N
                x += 1

            # print(total)
            return total

        # to_roman(2008) # MMVIII
        # to_roman(1666) # MDCLXVI
        # Larger than any number in the dataset
        # to_roman(11111) # MMMMMMMMMMMCXI
        # to_roman(4595) # MMMMDXCV
        # to_roman(4695) # MMMMDCXCV

        # from_roman('MMMMDXCV') # 4595
        # from_roman('MMMMDCXCV') # 4695
        # from_roman(to_roman(2008)) # 2008
        # from_roman(to_roman(1666)) # 1666
        # from_roman(to_roman(11111)) # 11111
        # from_roman('MMMMMMMMMMMCXI') # 11111

        def init(file_name):
            result_arr = []

            file_handler = open(correct_path_and_name(file_name))

            for line in file_handler:
                cleaned = line.replace('\n', '')
                result_arr.append(cleaned)

            return result_arr

        # ------------------------------------ #

        def solve():
            ALGO_BEGIN = time.time()

            data = init('data/project_euler_89_input.txt')
            result = 0

            for x in range(0, len(data), 1):
                orig_num = data[x]
                orig_len = len(orig_num)
                new_num = from_roman(orig_num) 
                new_len = len(to_roman(new_num))
                diff = orig_len - new_len

                # Should never be below 0, check math.
                if diff < 0:
                    raise Exception("Should never be below 0, check math.")

                result += (orig_len - new_len)
                msg(result_data, str(orig_num) + " can be made " + str(orig_len - new_len) + " more efficient")

            conclude(result_data, result, ALGO_BEGIN)
            
        solve() # 743

    except Exception as ex:
        print('Exception: ' + str(ex))