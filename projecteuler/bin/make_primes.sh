#!/usr/bin/env bash

echo "Factoring and initializing Prime Numbers up to 700_000_000 ... this may take up to 10 minutes"

python _make_and_print_primes.py --max_num 700000000 --file_name primes_to_700_mil &

python _make_and_print_primes.py --max_num 2000000 --file_name primes_to_2_mil &

wait