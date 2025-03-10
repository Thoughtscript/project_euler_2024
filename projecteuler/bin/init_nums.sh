#!/usr/bin/env bash

echo "Factoring and initializing Prime and Fibonacci Numbers up to 1_000_000_000 ... this may take up to 20 minutes"

python _make_and_print_fib.py --max_num 1000000000 &

python _make_and_print_primes.py --max_num 700000000 --file_name primes_to_700_mil &

python _make_and_print_primes.py --max_num 100000000 --file_name primes_to_100_mil &

python _make_and_print_primes.py --max_num 50000000 --file_name primes_to_50_mil &

python _make_and_print_primes.py --max_num 2000000 --file_name primes_to_2_mil &

wait