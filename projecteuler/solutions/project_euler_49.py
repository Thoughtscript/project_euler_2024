# https://projecteuler.net/problem=49
from lib import initialize, msg, conclude
import time
from data import primes_to_2_mil_map

if __name__ == '__main__':

    try:

        four_map = {}

        PRIME_MAP = primes_to_2_mil_map.primes

        result_data = initialize(49, str(296962999629), 0, 0, [])

        def is_prime(num):
            VAL = PRIME_MAP.get(num)
            result = not VAL is None
            return result

        def makeSortedKey(a,b,c,d):
            local_arr = [a,b,c,d]
            local_arr.sort()
            return ",".join(str(x) for x in local_arr)
        
        def make_key(arr):
            string_result = ""

            for x in range(0, len(arr), 1):
                string_result += str(arr[x])

            return string_result
        
        def permute(original_arr):
            transfer_arr = original_arr
            heaps_results = {}

            def swap(end, begin):
                original = transfer_arr[begin]
                transfer_arr[begin] = transfer_arr[end]
                transfer_arr[end] = original

            def heaps_algorithm(n):
                if n == 1: 
                    key = make_key(transfer_arr)
                    heaps_results[key] = key
                    return
            
                for i in range(0, n, 1):
                    heaps_algorithm(n-1)
                    v = 0
                    if n % 2 == 0:
                        v = i
                    swap(n-1, v)

            heaps_algorithm(len(original_arr))
            return heaps_results

        def makeFours():
            for a in range(0, 10, 1):
                for b in range(0, 10, 1):
                    for c in range(0, 10, 1):
                        for d in range(0, 10, 1):
                            heaps = permute([a,b,c,d])
                            key = makeSortedKey(a, b, c, d)
                            four_map[key] = heaps

        makeFours()

        def isValid(a, b, c):
            A = int(a)
            B = int(b)
            C = int(c)

            return  is_prime(A) and is_prime(B) and is_prime(C) and (C - B == B - A)

        def solve():
            ALGO_BEGIN = time.time()

            len_combos = len(four_map.keys())
            four_map_key_arr = list(four_map)

            for x in range(0, len_combos, 1):
                four_map_key_current = four_map_key_arr[x]
                four_map_current = four_map.get(four_map_key_current)
                four_map_key_current = list(four_map_current.keys())
                four_map_key_current_len = len(four_map_current.keys())
                four_map_key_current.sort()

                if four_map_key_current_len < 3:
                    continue

                for y in range(0, four_map_key_current_len, 1):
                    for z in range(y, four_map_key_current_len, 1):
                        if y == z:
                            continue

                        for w in range(z, four_map_key_current_len, 1):
                            if y == z or z == w or w == z: 
                                continue

                            A = four_map_key_current[y]
                            B = four_map_key_current[z]
                            C = four_map_key_current[w]

                            msg(result_data, "Trying: " + str(A) + " " + str(B) + " " + str(C))

                            if isValid(A, B, C):
                                conclude(result_data, str(A) + str(B) + str(C), ALGO_BEGIN) 
        
        solve()

        # Solution found: 0163 0613 1063
        # Solution found: 0379 3709 7039
        # Solution found: 1487 4817 8147
        # Solution found: 2969 6299 9629

        # Omitting the first two since they have leading 0's

    except Exception as ex:

        print('Exception: ' + str(ex))