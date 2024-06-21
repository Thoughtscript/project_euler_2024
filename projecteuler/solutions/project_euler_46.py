# https://projecteuler.net/problem=46
from lib import initialize, msg, conclude
import time
from data import primes_to_2_mil_map

if __name__ == '__main__':

    try:
       
        PRIME_MAP = primes_to_2_mil_map.primes

        result_data = initialize(46, 5777, 0, 0, [])

        def is_odd(num):
            return not num % 2 == 0
        
        def is_composite(num):
            return PRIME_MAP.get(num) is None
        
        def is_goldbach(num):
            for y in range(0, num, 1):
                current_prime = PRIME_MAP.get(y)

                if current_prime is None:
                    continue

                if y >= num:
                    return False
                
                for z in range(0, num, 1):
                    val = y + 2 * (z * z)
                    msg(result_data, "Testing sum of prime and twice a square: " + str(y) + " + 2 * " + str(z * z) + " = " + str(val))

                    if val == num:
                        return True
                    
                    if val > num:
                        break

            return False

        
        def solve():
            ALGO_BEGIN = time.time()
            
            for x in range(5750, 999_999, 1):
                if is_composite(x) and is_odd(x):
                    if not is_goldbach(x):
                        msg(result_data, "Smallest odd composite found for which Goldbachs Conjecture fails: " + str(x))
                        conclude(result_data, x, ALGO_BEGIN) 
                        return
                    #else:
                      # msg(result_data, "Goldbachs Conjecture holds for odd composite number: " + str(x))

        solve() # 5777

    except Exception as ex:

        print('Exception: ' + str(ex))