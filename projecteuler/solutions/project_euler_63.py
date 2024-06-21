# https://projecteuler.net/problem=63
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    try:   

        result_data = initialize(63, 49, 0, 0, [])

        def solve():
            ALGO_BEGIN = time.time()

            hm = {}
            count = 0
            for nth_root_of in range(0, 23, 1):
                for expon in range(0, 23, 1):
                    num = pow(nth_root_of, expon)
                    if hm.get(num) is None:
                        p = len(str(num))
                        if (expon == p):
                            msg(result_data, "Powerful Digit found: " + str(num) + " len&exp: " + str(p))
                            count +=1
                            hm[num] = True
                    else:
                        continue

            msg(result_data, "Total Powerful Digits found: " + str(count))
            count-=1
            msg(result_data, "Discounting 0 which is excluded: " + str(count))
            conclude(result_data, count, ALGO_BEGIN)
                  
        solve() # 49
        
        # 50 of which there are 28 before 9^exp
        ## Turns out 0 is excluded!!
        ## I was considering 0^1 to be valid: length == 1 == exp but it's apparently not-positive.

    except Exception as ex:

        print('Exception: ' + str(ex))

'''
Powerful Digit found: 0 len&exp: 1
Powerful Digit found: 1 len&exp: 1
Powerful Digit found: 2 len&exp: 1
Powerful Digit found: 3 len&exp: 1
Powerful Digit found: 4 len&exp: 1
Powerful Digit found: 16 len&exp: 2
Powerful Digit found: 5 len&exp: 1
Powerful Digit found: 25 len&exp: 2
Powerful Digit found: 125 len&exp: 3
Powerful Digit found: 6 len&exp: 1
Powerful Digit found: 36 len&exp: 2
Powerful Digit found: 216 len&exp: 3
Powerful Digit found: 1296 len&exp: 4
Powerful Digit found: 7 len&exp: 1
Powerful Digit found: 49 len&exp: 2
Powerful Digit found: 343 len&exp: 3
Powerful Digit found: 2401 len&exp: 4
Powerful Digit found: 16807 len&exp: 5
Powerful Digit found: 117649 len&exp: 6
Powerful Digit found: 8 len&exp: 1
Powerful Digit found: 64 len&exp: 2
Powerful Digit found: 512 len&exp: 3
Powerful Digit found: 4096 len&exp: 4
Powerful Digit found: 32768 len&exp: 5
Powerful Digit found: 262144 len&exp: 6
Powerful Digit found: 2097152 len&exp: 7
Powerful Digit found: 16777216 len&exp: 8
Powerful Digit found: 134217728 len&exp: 9
Powerful Digit found: 1073741824 len&exp: 10
Powerful Digit found: 9 len&exp: 1
Powerful Digit found: 81 len&exp: 2
Powerful Digit found: 729 len&exp: 3
Powerful Digit found: 6561 len&exp: 4
Powerful Digit found: 59049 len&exp: 5
Powerful Digit found: 531441 len&exp: 6
Powerful Digit found: 4782969 len&exp: 7
Powerful Digit found: 43046721 len&exp: 8
Powerful Digit found: 387420489 len&exp: 9
Powerful Digit found: 3486784401 len&exp: 10
Powerful Digit found: 31381059609 len&exp: 11
Powerful Digit found: 282429536481 len&exp: 12
Powerful Digit found: 2541865828329 len&exp: 13
Powerful Digit found: 22876792454961 len&exp: 14
Powerful Digit found: 205891132094649 len&exp: 15
Powerful Digit found: 1853020188851841 len&exp: 16
Powerful Digit found: 16677181699666569 len&exp: 17
Powerful Digit found: 150094635296999121 len&exp: 18
Powerful Digit found: 1350851717672992089 len&exp: 19
Powerful Digit found: 12157665459056928801 len&exp: 20
Powerful Digit found: 109418989131512359209 len&exp: 21
Total Powerful Digits found: 50
'''