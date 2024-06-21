# https://projecteuler.net/problem=37
from lib import initialize, conclude, msg
import time
from data import primes_to_2_mil_map

if __name__ == "__main__":

    try:

        result_data = initialize(37, 748317, 0, 0, [])

        PRIME_MAP = primes_to_2_mil_map.primes

        def is_prime(num_str):
            VAL = PRIME_MAP.get(int(num_str))
            result = not VAL is None
            return result

        # is_prime("101010")
        # is_prime("79")
        # is_prime("7")
        # is_prime("1382399")
            
        # A left to right and right to left truncatable prime:
        # Must start with 2, 3, 5, or 7
        # End with 2, 3, 5, or 7
        # Those are the only single digit primes.

        def is_truncatable(num_str):
            if not (num_str[0] == "2" or num_str[0] == "3" or num_str[0] == "5" or num_str[0] == "7"):
                # print(num_str + " is not a truncatable prime")
                return False

            LEN = len(num_str)
            LAST = num_str[LEN - 1]

            if not (LAST == "2" or LAST == "3" or LAST == "5" or LAST == "7"):
                # print(num_str + " is not a truncatable prime")
                return False

            for x in range(0, LEN, 1):
                # Left to Right
                temp_fwd = num_str[0+x:LEN]
                # Right to Left no reversal!
                temp_bwd = num_str[0:LEN-x]

                if is_prime(temp_fwd) and is_prime(temp_bwd):
                    continue
                else:
                    msg(result_data, num_str + " is not a truncatable prime")
                    return False

            msg(result_data, num_str + " is a truncatable prime")
            return True

        # is_truncatable("3797")
        # is_truncatable("20000")
        # is_truncatable("132321")
        # is_truncatable("13883")
        # is_truncatable("293213")
        # is_truncatable("5000")

        def solve():
            ALGO_BEGIN = time.time()

            result = []
            for x in range(0, 2000000, 1):
                if is_truncatable(str(x)):
                    print("Is truncatable prime found: " + str(x))
                    result.append(x)
            
            msg(result_data, "Found " + str(len(result)) + " truncatable primes")
            msg(result_data, "Result: " + str(result))

            sum = 0

            for x in range(0, len(result), 1):
                # Need to exclude 2,3,5,7 from answer
                if result[x] == 2 or result[x] == 3 or result[x] == 5 or result[x] == 7:
                    continue
                else:
                    sum += int(result[x])

            msg(result_data, "Sum found: " + str(sum))
            conclude(result_data, sum, ALGO_BEGIN)

        solve() # 748317

    except Exception as ex:

        print("Exception: " + str(ex))