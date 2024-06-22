# https://projecteuler.net/problem=112
from lib import initialize, msg, conclude
import time
from decimal import *

if __name__ == '__main__':

    try:

        result_data = initialize(112, 1587000, 0, 0, [])

        def increasing_or_decreasing(num):
            s = str(num)
            LEN = len(s)
            is_increasing = True
            is_decreasing = True

            for x in range(0, LEN, 1):
                if x < LEN - 1:
                    if int(s[x]) > int(s[x+1]) and is_increasing:
                        #msg(result_data, str(num) + " is not an increasing number")
                        is_increasing = False
                        
                if x > 0:
                    if int(s[x-1]) < int(s[x]) and is_decreasing:
                        #msg(result_data, str(num) + " is not a decreasing number")
                        is_decreasing = False

                if (not is_increasing and not is_decreasing):
                    break

            #if (is_increasing and not is_decreasing):
                #msg(result_data, str(num) + " is an increasing number")

            #if (not is_increasing and is_decreasing):
                #msg(result_data, str(num) + " is a decreasing number")

            return [is_increasing, is_decreasing]
            
        def is_bouncy(num):
            bools = increasing_or_decreasing(num)
            result = (bools[0] == False and bools[1] == False)
            # msg(result_data, str(num) + " is bouncy: " + str(result))
            return result

        # is_bouncy(155349)
        # is_bouncy(134468)
        # is_bouncy(66420)
        # is_bouncy(14232323232)
        # is_bouncy(1234566)

        def solve():
            ALGO_BEGIN = time.time()

            bouncy_count = 0

            for x in range(1, 3000000, 1):
                if is_bouncy(x):
                    bouncy_count = bouncy_count + 1

                ratio = Decimal(bouncy_count) / Decimal(x)
                # msg(result_data, "Ratio: " + str(ratio))

                # if ratio >=  Decimal(.5):
                #    print("Number found: " + str(x) + " ratio: " + str(ratio))
                #    return x
                # 
                # Expected: 538 Actual: 538

                if ratio >=  Decimal(.99):
                    msg(result_data, "Number found: " + str(x) + " ratio: " + str(ratio))
                    conclude(result_data, x, ALGO_BEGIN)
                    return

            msg(result_data, "None found!")
            return

        solve() # 1587000

    except Exception as ex:

        print('Exception: ' + str(ex))