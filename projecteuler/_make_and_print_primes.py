import argparse
from solutions import lib

if __name__ == '__main__':

    try:

        parser = argparse.ArgumentParser()
        parser.add_argument('--max_num')  
        parser.add_argument('--file_name')  
        args = parser.parse_args()

        print("Arguments received: [ max_num: " + str(args.max_num) + " file_name: " + str(args.file_name) + "]")

        '''
        SIEVE HELPERS
        '''
        def make_sieve_arr(max_num, do_print = False):
            sieve = lib.sieve_of_eratosthenes(max_num, do_print)
            primes = []

            for x in range(0, len(sieve), 1):
                if sieve[x] == True:
                    primes.append(x+1)

            if do_print:
                print(primes)

            return primes

        # Convert an Array of Prime Numbers (converted via the above) to a Map for O(1) lookup
        def sieve_arr_to_map(prime_arr, do_print = False):
            primes = {}

            for x in range(0, len(prime_arr), 1):
                primes[prime_arr[x]] = True
            
            if do_print:
                print(primes)

            return primes

        def make_and_print(max_num, file_name):
            prime_arr = make_sieve_arr(max_num, False)
            arr_file = open('solutions/data/' + file_name + '_arr.py', 'w')
            arr_file.write("primes=" + str(prime_arr)) # Make it easy to load
            arr_file.close()

            prime_map = sieve_arr_to_map(prime_arr, False)
            map_file = open('solutions/data/' + file_name + '_map.py', 'w')
            map_file.write("primes=" + str(prime_map)) # Make it easy to load
            map_file.close()

        make_and_print(int(args.max_num), args.file_name)

    except Exception as ex:

        print('Exception: ' + str(ex))