# project_euler

[![](https://img.shields.io/badge/Project-Euler-green.svg)](https://projecteuler.net/) [![](https://img.shields.io/badge/Python-3.12.2-yellow.svg)](https://www.python.org/downloads/release/python-2718/) 

![Badge](https://projecteuler.net/profile/Thoughtscript.png)

My Project Euler solutions.

Now with Docker, better standardization, optimization, improved logging, timing, validation of compatibility with Python 3.12+, vastly reduced file-sizes, and so on.

> Deprecated: https://github.com/Thoughtscript/_project_euler

## Use

### Docker

A dockerized container is provided as a last resort (for those finding it difficult to setup and validate Python 3):

```bash
docker-compose up
```

Static File Server:

> http://localhost:8000/public/index.html

Execute the Solutions within the container:

> http://localhost:8000/api/execute?problem=30

Project Euler recommends that solutions be able to run in a ~2-3-minute timeframe (`120` to `180`) but some dependencies may take a long time to load.

You can see the outputs [here](/projecteuler/solutions/out) along with the actual runtimes that you can verify locally.

### Local

Execute the Solutions locally :
```bash
cd projecteuler/solutions
python3 project_euler_11.py
```

Make Primes locally:
```bash
python3 _make_and_print_primes.py --max_num 700000000 --file_name primes_to_700_mil
python3 _make_and_print_primes.py --max_num 2000000 --file_name primes_to_2_mil
```