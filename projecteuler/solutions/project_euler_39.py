# https://projecteuler.net/problem=39
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    try:

        result_data = initialize(39, 840, 0, 0, [])

        P = 1000

        def hashKey(a, b, c):
            local_arr = [a, b, c]
            local_arr.sort()
            return ",".join(str(x) for x in local_arr)

        def isRightTriangle(a, b, c):
            if c >= b and c >= a:
                return pow(c, 2) == pow(a, 2) + pow(b, 2)
            
            if b >= a and b >= c:
                return pow(b, 2) == pow(c, 2) + pow(a, 2)
            
            if a >= b and a >= c:
                return pow(a, 2) == pow(c, 2) + pow(b, 2)
            
        def solve():
            ALGO_BEGIN = time.time()

            global_max = 0
            maxed_p = 0

            for p in range(1, P, 1):
                local_hash = {}
            
                for a in range(1, p, 1):

                    for b in range(1, p, 1):
                        if a + b > p:
                            break

                        c = p - a - b
                        if c <= 0:
                            break

                        if a + b + c == p:
                            if isRightTriangle(a, b, c):
                                key = hashKey(a, b, c)
                                local_hash[key] = True
                
                local_max = len(local_hash.keys())

                if global_max < local_max:
                    global_max = local_max
                    maxed_p = p
                    msg(result_data, "New global_max found: " + str(local_max) + " for p: " + str(maxed_p))

            msg(result_data, "Maxed p found: " + str(maxed_p))
            conclude(result_data, maxed_p, ALGO_BEGIN)
            
        solve() # 840

        # New global_max found: 1 for p: 12
        # New global_max found: 2 for p: 60
        # New global_max found: 3 for p: 120
        # New global_max found: 4 for p: 240
        # New global_max found: 5 for p: 420
        # New global_max found: 6 for p: 720
        # New global_max found: 8 for p: 840
        # Maxed p found: 840

    except Exception as ex:

        print('Exception: ' + str(ex))