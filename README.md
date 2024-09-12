# project_euler

[![](https://img.shields.io/badge/Project-Euler-green.svg)](https://projecteuler.net/) [![](https://img.shields.io/badge/Python-3.12.2-yellow.svg)](https://www.python.org/downloads/release/python-2718/) 

![Badge](https://projecteuler.net/profile/Thoughtscript.png)

My Project Euler solutions. Wasn't a Math Major but really enjoy Mathematical Logic (from my Philosophy background) and came to enjoy Math later in life!

Now with Docker, better standardization, optimization, improved logging, timing, validation of compatibility with Python 3.12+, vastly reduced file-sizes, and so on.

> Deprecated: https://github.com/Thoughtscript/_project_euler

## Use

### Docker

A dockerized container is provided as a last resort (for those finding it difficult to setup and validate Python 3):

```bash
docker-compose up
```

Project Euler recommends that solutions be able to run in a `~2-3-minute` timeframe (duration `120` to `180`) but some dependencies may take a long time to load.

> You can also see the outputs [here](/projecteuler/solutions/out) along with the actual runtimes that you can verify locally.

Static File Server to display results like [Stephan Brumme](https://euler.stephan-brumme.com/) and detailed breakdowns like [Martin Ueding](https://martin-ueding.de/posts/project-euler-solution-70-totient-permutation/): 

> http://localhost:8000/public/index.html

Execute the Solutions within the container:

> http://localhost:8000/api/execute?problem=30

The default number of `uvicorn` workers is set to [4](./projecteuler/dockerfile) so one can execute multiple Solutions simultaneously in a non-blocking way. Feel free to modify those settings.
 
If you need to disable the initial Prime Number generators comment out the respective lines [here](./projecteuler/bin/make_primes.sh).

### Local

Execute the Solutions locally :
```bash
cd projecteuler/solutions
python3 project_euler_11.py
```

Make Primes locally:
```bash
python3 _make_and_print_primes.py --max_num 2000000 --file_name primes_to_2_mil
python3 _make_and_print_primes.py --max_num 50000000 --file_name primes_to_50_mil
python3 _make_and_print_primes.py --max_num 100000000 --file_name primes_to_100_mil
python3 _make_and_print_primes.py --max_num 700000000 --file_name primes_to_700_mil 

# This can take between 5-20 minutes depending on your hardward/configuration.
```

> This is the same kind of approach most of the "Big Dogs" take W.R.T. prime factor/number calculations - one can use whatever library they like to complete the problems in the spirit and intent of Project Euler and many folks pregenerate prime numbers Ahead-of-Time (AOT precomputation) thereby.

## Performance

Do be forewarned that Memory (RAM, Volatile) use might be quite high depending on the approach you choose to take:

1. The generated file `primes_to_700_mil_map.py` is about `520mb` and can be quickly run if you execute the provided [Bash](./projecteuler/bin/make_primes.sh) script outside of Docker:  
   * Running a problem that loads that dependency (such as [problem 58](./projecteuler/solutions//project_euler_58.py)) is very quick outside of Docker but might be very slow within Docker.
   * Should only peak at about `3GB`.
1. Your mileage might vary based on other settings/configurations including **Docker**, **Windows Linux Subsystem**:
   * Docker on WSL will use upwards of `20GB` for such problems. (Possibly necessitating modifying ones `.wslconfig` as [I found out](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#wslconfig)!)
   * I have not yet found a faster approach - apparently this algo [`make_optimized_sieve_arr`](./projecteuler/_make_and_print_primes.py) is pretty close to the known fastest implementation without parallelization. (It's my own implementation and I don't just want to copy some other person's faster one!)