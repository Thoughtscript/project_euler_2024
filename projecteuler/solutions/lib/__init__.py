import time
import json
import os

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

def correct_path_and_name(file_name):
    file_path = 'data/'
    if os.path.exists(file_path):
        return file_path + file_name
    
    file_path = 'solutions/data/'
    if os.path.exists(file_path):
        return file_path + file_name

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

def initialize(problem = -1, expected = -1, actual = -1, duration = 0, output = [], passed = False):
    output.append("Running solution for problem: " + str(problem))
    output.append("Expected result: " + str(expected))

    return { 
        "problem": problem, 
        "expected": expected, 
        "actual": actual, 
        "duration": duration, 
        "output": output,
        "passed": passed,
    }

def msg(result_data, message):
    result_data['output'].append(message)

def check_path_exist(file_path, file_name, parsed):
    if os.path.exists(file_path):
        result_data_json = open(file_path + file_name, 'w')
        result_data_json.write(json.dumps(parsed, indent=4))
        result_data_json.close()

def print_result_data_json(result_data):
    result_data_temp = result_data
    result_data_temp["problem"] = str(result_data_temp["problem"])
    result_data_temp["expected"] = str(result_data_temp["expected"])
    result_data_temp["actual"] = str(result_data_temp["actual"])
    result_data_temp["duration"] = str(result_data_temp["duration"])
    result_data_temp["passed"] = str(result_data_temp["passed"])

    result_data_as_string = str(result_data_temp)
    result_data_as_string = result_data_as_string.replace("'", "\"")
    parsed = json.loads(result_data_as_string)
    file_name = 'project_euler_' + str(result_data['problem']) + '.json'

    check_path_exist('out/', file_name, parsed) # local
    check_path_exist('solutions/out/', file_name, parsed) # from relative path of executed Bash command

def conclude(result_data, solution, begin):
    ALGO_END = time.time()
    msg(result_data, "Solution found: " + str(solution))
    result_data['actual'] = solution
    result_data['duration'] = ALGO_END - begin
    result_data['passed'] = result_data['actual'] == result_data['expected']
    print(result_data)
    print_result_data_json(result_data)

'''
LIST HELPER
'''

def sum_list(lst):
    total = 0

    for x in range(0, len(lst), 1):
        total += int(lst[x])

    return total

# Primarily for converting an Array of Prime Numbers (converted via the above) to a Map for O(1) lookup
def list_to_map(lst, do_print = False):
    mp = {}

    for x in range(0, len(lst), 1):
        mp[lst[x]] = True
            
    if do_print:
        print(mp)

    return mp