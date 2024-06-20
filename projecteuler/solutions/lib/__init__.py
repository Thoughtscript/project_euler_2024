import time

'''
PRIME NUMBERS
'''
# Brute-Force a Prime
def check_prime(num):
    SQ_RT = pow(num, 1/2)

    for x in range(2, SQ_RT+1, 1):
        if num % x == 0:
            return False

    return True

# Generate an 0-indexed array where:
# sieve[i] = False indicates non-prime
# sieve[i] = True indicates prime
def sieve_of_eratosthenes(max_num, do_print=False):
    sieve = [0] * max_num
    sieve[0] = False
            
    for x in range(2, max_num+1, 1):
        # The following will throw a Warning since it compares Literals
        # 'if sieve[x-1] is 0:'
        
        # Note that 0 is 0 // True
        # But False is 0 // False
        if sieve[x-1] == 0 and not sieve[x-1] is False:
            sieve[x-1] = True

        for y in range(x*2, max_num+1, x):
            sieve[y-1] = False

    if do_print:
        print(sieve)

    return sieve

# Offset num by one when accessing
def prime_factorization(max_num, do_print=False):
    primes = sieve_of_eratosthenes(max_num, do_print)
    result = []
    rem = max_num

    while rem % 2 == 0:
        rem = rem / 2
        result.append(2)

    # Must be odd or not divisible by 2 once it reaches here
    for x in range(3, max_num+1, 2):
        if (primes[x-1] == False):
            continue

        while (rem % x == 0):
            result.append(x)
            rem = rem / x

        if rem == 1 or rem == 0:
            break

    if do_print:
        print(result)

    return result

def number_of_divisors(max_num, do_print=False):
    prime_factors = prime_factorization(max_num, do_print)
    result = 1
    hm = {}

    for x in range(0, len(prime_factors), 1):
        n = prime_factors[x]

        if not hm.get(n) is None:
            hm[n] = hm[n] + 1
        else:
            hm[n] = 1

    keys = hm.keys()
            
    for x in range(0, len(keys), 1):
        n = hm[keys[x]]
        result = result * (n + 1)

    if do_print:
        print(result)

    return result

'''
INPUT FILES
'''
import json

def load_json_file(file_name, do_print=False):
    jsonAsString = ""

    fileHandler = open(file_name + '.json')
    for line in fileHandler:
        jsonAsString += line

    entries = json.loads(jsonAsString)

    if do_print:
        print(entries)

    return entries

def load_txt_file_as_list(file_name, do_print=False):
    result_list = []

    fileHandler = open(file_name + '.txt')
    for line in fileHandler:
        result_list.append(line.split(","))
    
    if do_print:
        print(result_list)

    return result_list

'''
STDOUT
'''

def initialize(problem = -1, expected = -1, actual = -1, duration = 0, output = []):
    output.append("Running solution for problem: " + str(problem))
    output.append("Expected result: " + str(expected))

    return { 
        "problem": problem, 
        "expected": expected, 
        "actual": actual, 
        "duration": duration, 
        "output": output
    }

def msg(result, message):
    result['output'].append(message)

def conclude(result, solution, begin):
    ALGO_END = time.time()
    msg(result, "Solution found: " + str(solution))
    result['actual'] = solution
    result['duration'] = ALGO_END - begin
    print(result)

