# https://projecteuler.net/problem=33
from lib import initialize, msg, conclude
import time
from decimal import *

if __name__ == '__main__':

    try:

        result_data = initialize(33, 100, 0, 0, [])
        
        def solve():
            ALGO_BEGIN = time.time()

            non_trivial = []

            max_val = 100
            # numerator and denominator must both have two digits
            for numerator in range(10, max_val, 1):
                num_str = str(numerator)

                for denominator in range(10, max_val, 1):
                    den_str = str(denominator)

                    fraction = Decimal(numerator) / Decimal(denominator)
                    if fraction >= 1:
                        continue

                    if not int(den_str[1]) == 0 and fraction == Decimal(int(num_str[0])) /  Decimal(int(den_str[1])) and int(num_str[1]) == int(den_str[0]):
                        msg(result_data, "Non-trivial cancelling fraction found: " + num_str + "/" + den_str)
                        non_trivial.append(fraction)

                    if not int(den_str[0]) == 0 and  fraction == Decimal(int(num_str[1])) /  Decimal(int(den_str[0])) and int(num_str[0]) == int(den_str[1]):
                        msg(result_data, "Non-trivial cancelling fraction found: " + num_str + "/" + den_str)
                        non_trivial.append(fraction)

            product = Decimal(1)

            for x in range(0, len(non_trivial), 1):
                product = product * non_trivial[x]

            # 1/100 -> 100 is the denominator
            msg(result_data, str(product) + " found - taking 1/(" + str(product) +") to return the denominator")
            conclude(result_data, int(1 / product), ALGO_BEGIN)

        solve()


    except Exception as ex:

        print('Exception: ' + str(ex))