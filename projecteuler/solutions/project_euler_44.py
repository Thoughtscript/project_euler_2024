# https://projecteuler.net/problem=44
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    try:

        result_data = initialize(44, 5482660, 0, 0, [])

        pentagonal_map = {}
        pentagonal_arr = []
        num_pentagonals = 99999

        def makePentagonal(n):
            return n * (3 * n - 1) / 2
        
        def isPentagonal(n):
            check_pentagonal = pentagonal_map.get(n)
            if not check_pentagonal:
                return False
            return True
        
        def generatePentagonals():
            for x in range(1, num_pentagonals, 1):
                pentagonal = makePentagonal(x)
                pentagonal_map[pentagonal] = True
                pentagonal_arr.append(pentagonal)

            msg(result_data, "First " + str(num_pentagonals) + " pentagonals generated!")
        
        def calcPair(x, y):
            S = x + y
            D = abs(x - y)

            if (isPentagonal(S) and isPentagonal(D)):
                 return D

            return False
        
        def solve():
            ALGO_BEGIN = time.time()

            generatePentagonals()

            minimized_d = 99999999999999

            for x in range(0, num_pentagonals - 1, 1):
                for y in range(0, num_pentagonals - 1,1):
                    if x == y:
                        continue

                    X = pentagonal_arr[x]
                    Y = pentagonal_arr[y]
                    D = calcPair(X, Y)

                    if D is not False:
                        if minimized_d > D:
                            minimized_d = D
                            msg(result_data, "New minimized_D found: " + str(D) + " for X:" + str(X) + " Y:" + str(Y))
                            # if isPentagonal(X):
                            #     msg(result, str(X) + " is Pentagonal")
                            # else:
                            #     msg(result, str(X) + " is wrong!")

                            # if isPentagonal(Y):
                            #     msg(result, str(Y) + " is Pentagonal")
                            # else:
                            #     msg(result, str(Y) + " is wrong!")

                            # if isPentagonal(X+Y):
                            #     msg(result, str(X+Y) + " is Pentagonal")
                            # else:
                            #     msg(result, str(X+Y) + " is wrong!")

                            # if isPentagonal(D):
                            #     msg(result, str(D) + " is Pentagonal")
                            # else:
                            #     msg(result, str(D) + " is wrong!")

            if minimized_d == 99999999999999:
                msg(result_data, "No solution found for: " + str(num_pentagonals) + "-many pentagonals")
                return
            
            msg(result_data, "Solution found: " + str(minimized_d))
            conclude(result_data, minimized_d, ALGO_BEGIN)

        solve() # 5482660

    except Exception as ex:
        print('Exception: ' + str(ex))