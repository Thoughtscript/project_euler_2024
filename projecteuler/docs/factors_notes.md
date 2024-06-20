# Prime Factorization

1. https://www.mathsisfun.com/prime-factorization.html
2. https://www.geeksforgeeks.org/prime-factor/
3. https://www.math.drexel.edu/~tolya/220_euclid.pdf

```
So, all numbers are either primes or not.
All primes are divisible only by themselves and 1.
All non-primes can actually be represented as prime factors! (E.g. - they are composite numbers.)

Divide a number n by 2 repeatedly until it can't be cleanly divided.
Note that dividing by 2 cleanly until it can't be done anymore results in only odd divisors
Then continue to check through the next primes in the same way until the total amount of all primes multiplied together is greater than n.

12 is 2 x 2 x 3
18 is 2 x 3 x 3
```

> Compare the prime factors of a numerator and denominator to determine if maximally reduced fraction.

# Sieve of Eratosthenes

1. https://www.geeksforgeeks.org/sieve-of-eratosthenes/
2. https://byjus.com/maths/sieve-of-eratosthenes/

```
1. Define an array of length n equal to the target max number. Init each value to true or false (for is prime or not).
2. Each non-prime number will have at least one other divisor besides itself and 1. 
3. So, by finding every multiple of i from 1 to n (for each i), one can quickly identify any non-primes! (Divisible by i and >= to the square of i - the second clause prevents numbers from being checked twice.)
4. The remaining numbers are primes.
```

# Number of Divisors

1. https://www.geeksforgeeks.org/total-number-divisors-given-number/
2. https://www.geeksforgeeks.org/count-divisors-n-on13/
3. https://www.math.drexel.edu/~tolya/220_euclid.pdf
4. https://www.wikihow.com/Determine-the-Number-of-Divisors-of-an-Integer

```
1. Use the Sieve of Eratosthenes
2. Find all prime factors for n.
3. Multiple each prime factor exponent adding one to each multiple 1: d(24) = (3+1)(1+1) = 2 x 2 x 2 x 3
4. So, there are 8 divisors for 24: 1,2,3,4,6,8,12,24
```

# Euler's Totient Function

1. https://cp-algorithms.com/algebra/phi-function.html

'''
1. Finds all of the coprimes relative to a number.
2. Can be used to find all maximally reduced proper fractions up to some number n.
'''