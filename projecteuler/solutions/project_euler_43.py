# https://projecteuler.net/problem=43
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    try:

        result_data = initialize(43, 16695334890, 0, 0, [])

        # Same set of triples is use for each 3-length sub-strings.
        # Generate once and use for all.
        def make_triples():
            result = []

            for a in range(0, 10, 1):
                for b in range(0, 10, 1):
                    if a == b:
                        continue

                    for c in range(0, 10, 1):
                        if a == c or b == c:
                            continue

                        result.append(str(a) + str(b) + str(c))
            
            return result

        TRIPLES = make_triples()

        def includes(a, b):
            num_str = str(a)
            for x in range(0, len(num_str), 1):
                if int(num_str[x]) == int(b):
                    return True
            return False

        # Cannot brute force the strings above: 10 x 720 x 720 x 720.
        # Must use string compression (or something faster): 3,628,800 vs. 3,732,480,000.
        def solve():
            ALGO_BEGIN = time.time()

            result = []

            LEN = len(TRIPLES)

            for x in range(0, 10, 1):

                for a in range(0, LEN, 1):
                    A = TRIPLES[a]

                    tempA = str(x) + A

                    if not int(tempA[1] + tempA[2] + tempA[3]) % 2 == 0:
                        continue

                    if includes(A, x):
                        continue

                    for b in range(0, LEN, 1):
                        B = TRIPLES[b]

                        tempB = tempA + B

                        if not int(tempB[2] + tempB[3] + tempB[4]) % 3 == 0:
                            continue

                        if not int(tempB[3] + tempB[4] + tempB[5]) % 5 == 0:
                            continue

                        if not int(tempB[4] + tempB[5] + tempB[6]) % 7 == 0:
                            continue

                        if a == b:
                            continue

                        if includes(B, x):
                            continue

                        found = False

                        for y in range(0, len(B), 1):
                            if includes(A, B[y]):
                                found = True
                                break

                        if found:
                            continue

                        for c in range(0, LEN, 1):
                            C = TRIPLES[c]

                            tempC = tempB + C

                            if not int(tempC[5] + tempC[6] + tempC[7]) % 11 == 0:
                                continue

                            if not int(tempC[6] + tempC[7] + tempC[8]) % 13 == 0:
                                continue

                            if not int(tempC[7] + tempC[8] + tempC[9]) % 17 == 0:
                                continue

                            if a == c or b == c:
                                continue

                            if includes(C, x):
                                continue

                            found = False

                            for z in range(0, len(C), 1):
                                if includes(B, C[z]) or includes(A, C[z]):
                                    found = True
                                    break

                            if found:
                                continue

                            num_str = str(x) + A + B + C
                            msg(result_data, "Pandigital Number made: " + str(num_str))
                            result.append(int(num_str))

            msg(result_data, "Number of Pandigital Numbers is: " + str(len(result)))

            sum_result = 0

            for x in range(0, len(result), 1):
                sum_result += int(result[x])

            msg(result_data, "Sum is: " + str(sum_result))
            conclude(result_data, sum_result, ALGO_BEGIN)
            return sum_result

        solve() # 16695334890
        

    except Exception as ex:

        print('Exception: ' + str(ex))