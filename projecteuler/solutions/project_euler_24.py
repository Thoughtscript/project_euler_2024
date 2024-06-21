# https://projecteuler.net/problem=24
from lib import initialize, conclude
import time

if __name__ == '__main__':

    try:

        result_data = initialize(24, 2783915460, 0, 0, [])

        # Base cases: 0,123,456,789 -> 9,876,543,210

        def anyEqualsAny(arr):
            for x in range(0, len(arr), 1):
                for y in range(0, len(arr), 1):
                    if x == y:
                        continue
                    if arr[x] == arr[y]:
                        return True
            return False

        # 012 -> 021 -> 120 -> 201 ... 210
        # I'm assuming that 0123456789 -> 0123456798 for my initial run. 
        # This may be incorrect since the scenario's ambiguous (second col or second to last col change).
        # It does end in 987,6543,210

        def generate():
            result = []
            for a in range(0,10,1):
                for b in range(0,10,1):
                    if anyEqualsAny([a,b]):
                        continue

                    for c in range(0,10,1):
                        if anyEqualsAny([a,b,c]):
                            continue

                        for d in range(0,10,1):
                            if anyEqualsAny([a,b,c,d]):
                                continue

                            for e in range(0,10,1):
                                if anyEqualsAny([a,b,c,d,e]):
                                    continue

                                for f in range(0,10,1):
                                    if anyEqualsAny([a,b,c,d,e,f]):
                                        continue

                                    for g in range(0,10,1):
                                        if anyEqualsAny([a,b,c,d,e,f,g]):
                                            continue

                                        for h in range(0,10,1):
                                            if anyEqualsAny([a,b,c,d,e,f,g,h]):
                                                continue

                                            for i in range(0,10,1):
                                                if anyEqualsAny([a,b,c,d,e,f,g,h,i]):
                                                    continue

                                                for j in range(0,10,1):
                                                    if anyEqualsAny([a,b,c,d,e,f,g,h,i,j]):
                                                        continue

                                                    numStr = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i) +  str(j)
                                                    result.append(numStr)

            return result

        def solve():
            ALGO_BEGIN = time.time()

            result = generate()
            solution = result[999999]
            
            conclude(result_data, int(solution), ALGO_BEGIN) 

        solve() # 2783915460

    except Exception as ex:
        print('Exception: ' + str(ex))