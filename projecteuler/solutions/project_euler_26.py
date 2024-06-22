# https://projecteuler.net/problem=26
from lib import initialize, conclude, msg
import time
from decimal import *
import re
from data import project_euler_26_inputs as INPUT # This was generated line 115 below...

if __name__ == '__main__':

    try:

        result_data = initialize(26, 983, 0, 0, [])

        def includes(arr, b):
            for x in range(0, len(arr), 1):
                if arr[x] == b:
                    return True
            return False

        def prune(num_str):
            hm = {}

            for x in range(0, len(num_str), 1):

                check = hm.get(num_str[x])
                if check is None:
                    hm[num_str[x]] = 1
                else:
                    hm[num_str[x]] = hm[num_str[x]] + 1

            vals = hm.values()

            if len(vals) == 1:
                return num_str[0]

            return num_str

        def find_next_cycle(l, fraction_str):
            LEN = len(fraction_str)

            for r in range(1, LEN, 1):
                cycle_str = fraction_str[l:l+r]
                LEN_CYCLE = len(cycle_str)
                remaining_str = fraction_str[l+r:LEN]

                # Adjust remaining_str so that last rounded digit or incomplete cycles are ignored.
                adjust = LEN_CYCLE
                while not len(remaining_str) % LEN_CYCLE == 0:
                    adjust += 1
                    remaining_str = fraction_str[l+r:LEN - adjust]

                matches = re.findall(cycle_str, remaining_str)
                LEN_MATCHES = len(matches)
                LEN_REM =  len(remaining_str)

                # Remaining string must be cleanly partitioned by cycle.
                CLEANLY_DIVIDES = LEN_REM  / LEN_CYCLE == LEN_MATCHES
                NO_DIVIDES_REMAINDER = LEN_REM % LEN_CYCLE == 0

                if LEN_MATCHES > 1 and NO_DIVIDES_REMAINDER and CLEANLY_DIVIDES:
                    # print("Cycle found: " + cycle_str + " " + str(matches))

                    # First cycle should be the only valid one.
                    return prune(cycle_str)

                if LEN_MATCHES < 1:
                    break

            return ''

        def solve(PREC):
            ALGO_BEGIN = time.time()
            
            numerator = 1
            mx = 0
            mx_denominator = 2
            # hm = {}
            hm = INPUT.map

            # Set precision
            getcontext().prec = PREC
            
            for denominator in range(2, 1000):
                fraction = Decimal(numerator) / Decimal(denominator)
                KEY = str(numerator) + "/" + str(denominator)
                msg(result_data, "Fraction: " +  KEY)

                fraction_str = str(fraction)
                LEN = len(fraction_str)
                # print(fraction_str)

                # Hashed values can be skipped
                VAL = hm.get(KEY)
                if not VAL is None:
                    # print("Hashed values found:")
                    # print(VAL)
                    if VAL[1] >= mx:
                        mx = VAL[1]
                        mx_denominator = int(KEY[2:len(KEY)])
                        # print("Key " + KEY + " Denominator " + str(mx_denominator))
                        msg(result_data, "Largest recurring cycle found: " + VAL[0] + " length " + str(VAL[1]))
                    continue

                # Repeating will go to the max precision
                if LEN < PREC:
                    msg(result_data, "No cycle found ... skipping")
                    continue

                # 0.001420 
                # Need to block off any no-repeating part.
                # .......4545454545454
                # Start after decimal.
                for l in range(2, LEN-1, 1):
                    check = find_next_cycle(l, fraction_str)
                    reduced_string = fraction_str[0:l] + "(" + check + ")"

                    if len(check) > 0:
                        msg(result_data, "Recurring cycle found: " + check + " length " + str(len(check)) + " reduced form: " + reduced_string)
                        # hm[KEY] = [check, len(check), reduced_string]

                    if len(check) >= mx:
                        mx = len(check)
                        mx_denominator = denominator
                        msg(result_data, "Largest recurring cycle found: " + check + " length " + str(len(check)))
                        break

                    if len(check) > 0:
                        break

            msg(result_data, hm)
            msg(result_data, "Largest recurring cycle found: " + str(mx) + " for denominator: " + str(mx_denominator))

            no_cycle = []
            for denominator in range(2, 1000):
                check = hm.get(str(numerator) + "/" + str(denominator))
                if check is None:
                    no_cycle.append(str(numerator) + "/" + str(denominator))

            msg(result_data, "No cycles found (possibly non-terminating):")
            msg(result_data, no_cycle)
            conclude(result_data, mx_denominator, ALGO_BEGIN) 
            
        # The value parameterized here matters - it must be large enough for full cycles to be found.
        # From: Mitchell and Dickson - the repetend length period of 1/k is always <= k - 1.
        solve(5000) 
        
        # It's actually much much faster with higher precsision!
        # Denominator 799 had largest repetend length 368 using precision 1500
        # Denominator 983 had largest repetend length 982 using precsision 5000

    except Exception as ex:

        print('Exception: ' + str(ex))