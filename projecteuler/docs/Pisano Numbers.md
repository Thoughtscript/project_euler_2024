# Pisano Numbers

Picked up the following for fun:
1. https://projecteuler.net/problem=853
2. https://www.codewars.com/kata/65de16794ccda6356de32bfa
3. https://www.codewars.com/kata/5f1360c4bc96870019803ae2
4. https://projecteuler.net/problem=854

I really don't like *just* copy-pasting others' answers - and most I've seen would neverthless fail **3.** (the easiest) anyway.

For example:
1. https://stackoverflow.com/questions/62585865/pisano-period-length-finding
2. https://medium.com/competitive/huge-fibonacci-number-modulo-m-6b4926a5c836#.8n3hmh3el
3. My answer below (which is a fairly run-of-the-mill approach apparently that comes from the Wikipedia description: https://en.wikipedia.org/wiki/Pisano_period

Bit stumped and thinking through optimizations to the above (and below)! I've consulted the other solutions for some trick or shortcut at last resort!

Alas! I don't see easy solutions to generate the result in sub-linear time, up to `1_000_000_000` per the Project Euler problem, etc.

## My Naive Approach

Is accurate apparently:

```python
import math

powers_two = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432]
powers_five = [5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625, 48828125, 244140625, 1220703125, 6103515625]

def found_new_cycle(seq, current):       
    if current < 4:
        return False
            
    A = seq[0] == 0
    B = seq[1] == 1
            
    return A and B

# https://oeis.org/A001175
def pisano(n):
    # From:  https://en.wikipedia.org/wiki/Pisano_period#Number_of_zeros_in_the_cycle
    ## Every Pisano sequence starts with 0,1

    if n == 1:
        return 1
        
    if n == 2:
        return 3
    
    if n in powers_two:
        return 3 * n / 2
    
    if n in powers_five:
        return 4 * n

    fibs = [0,1]
    current = 0 # Use this so don't have to use Hexadecimal cipher 
                # by comparing len(seq)
                ## offset by 2
    
    seq = [0,1] # Use list or dict not string

    while (not found_new_cycle(seq, current)):
        fib = fibs[len(fibs) - 1] + fibs[len(fibs) - 2] 
                
        seq[0] = seq[1]
        seq[1] = fib % n

        fibs[0] = fibs[1]
        fibs[1] = fib
        current += 1

    return current
```

Append test data:

```python
TEST_DATA = [
  1,3,8,6,20,24,16,12,24,60,10,24,28,48,40,24,36,24,18,60,16,30,48,24,100,84,72,48,14,120,30,48,40,
  36,80,24,76,18,56,60,40,48,88,30,120,48,32,24,112,300,72,84,108,72,20,48,72,42,58,120,60,30,48,96,
  140,120,136,36,48,240,70,24,148,228,200,18,80,168,78,120,216,120,168,48,180,264,56,60,44,120,112,
  48,120,96,180,48,196,336,120,300,50,72,208,84,80,108,72,72,108,60,152,48,76,72,240,42,168,174,144,
  120,110,60,40,30,500,48,256,192,88,420,130,120,144,408,360,36,276,48,46,240,32,210,140,24
] # len 144
        
def run_test():
    test_buffer = []
    MX_NUM_IDX = 250 # tweak this

    for n in range(0, MX_NUM_IDX, 1):
        test_buffer.append(pisano(n+1))

    print(test_buffer)

    for x in range(0, MX_NUM_IDX, 1):
        if x >= len(test_buffer) or x >= len(TEST_DATA):
            break

        if not TEST_DATA[x] == test_buffer[x]:
            raise Exception("Mismatching pisano numbers detected! " + str(TEST_DATA[x]) + " " + str(test_buffer[x]) + " at index: " + str(x))
        
run_test()
```

The above (and the other excellent solutions appear to correctly generate the Pisano Numbers but too slowly yet... at least with my tinkering...)

> Will attempt to figure this out for https://github.com/Thoughtscript/project_euler_2024! Also, creating this since there's a grouping of interesting problems. Also, a bunch of unsolved math problems (and not just mine! The community's).

## Improvements

So, I guess this is the root cause per: https://www.geeksforgeeks.org/fibonacci-number-modulo-m-and-pisano-period/

```python
    fibs[0] = fibs[1]
    fibs[1] = fib
```

By tweaking the above to not track or hold `fib` values whilst keeping the `powers_of` I can make a faster solution than the fully general **geeksforgeeks** solution (on Codewars), halve my original solution with the **geeksforgeeks** suggestion, while passing the execution time requirements (baking the cake and eating it too - hooray!):

```python
import math

# Greedily precomputed for stated cases
powers_two = {
    2: True, 
    4: True, 
    8: True, 
    16: True, 
    32: True, 
    64: True, 
    128: True, 
    256: True, 
    512: True, 
    1024: True, 
    2048: True, 
    4096: True, 
    8192: True, 
    16384: True, 
    32768: True, 
    65536: True, 
    131072: True, 
    262144: True, 
    524288: True#, 
    #1048576: True
}

powers_five = {
    5: True, 
    25: True, 
    125: True, 
    625: True, 
    3125: True, 
    15625: True, 
    78125: True,
    390625: True,
    1953125: True, 
    9765625: True#, 
    #48828125: True
}

def found_new_cycle(seqA, seqB, current):       
    if current < 4:
        return False
                        
    return seqA == 0 and seqB == 1

# https://oeis.org/A001175
def pisano(n):
    # From: https://en.wikipedia.org/wiki/Pisano_period#Number_of_zeros_in_the_cycle
    ## Every Pisano sequence starts with 0,1

    if n == 1:
        return 1
        
    if n == 2:
        return 3
    
    # Seeing how powers interact with the sequences
    ## Keeping this in actually halves the total runtime.
    ## dunno if that holds generally for the specific cases...
    if not powers_two.get(n) is None:
        return 3 * n // 2
    
    if not powers_five.get(n) is None:
        return 4 * n

    current = 0 # Use this so don't have to use Hexadecimal cipher 
                # by comparing len(seq)
                ## offset by 2
    
    seqA, seqB = 0,1 # Use int vals not string, dict, or list

    while (not found_new_cycle(seqA, seqB, current)):
        f = seqA + seqB
        seqA = seqB
        seqB = f % n
        current += 1

    return current
```

I guess that `(fibs[0] + fibs[1]) % n == (seq[0] + seq[1]) % n` at each iteration. I did not see that!

```python
    fibs = [0,1]
    current = 0 # Use this so don't have to use Hexadecimal cipher 
                ## by comparing len(seq)
                ## offset by 2
    
    seq = [0,1] # Use list or dict not string

    while (not found_new_cycle(seq, current)):
        fib = fibs[0] + fibs[1] 
        f = seq[0] + seq[1]
        
        seq[0] = seq[1]
        #seq[1] = fib % n
        seq[1] = f % n
        
        print(fib % n == f % n)

        fibs[0] = fibs[1]
        fibs[1] = fib
        current += 1

    return current
```

The above proves that programmatically. Still need to think through the deeper mathematical relationships..