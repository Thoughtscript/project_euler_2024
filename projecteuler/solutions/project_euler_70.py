# https://projecteuler.net/problem=243
from lib import initialize, msg, conclude
import time
from data import primes_to_50_mil_arr
from decimal import *

if __name__ == '__main__':

    try:

        result_data = initialize(70, 8_319_823, 0, 0, [])

        PRIMES = primes_to_50_mil_arr.primes

        # https://cp-algorithms.com/algebra/phi-function.html
        ## I was just introduced to this technique
        ### This is simplified to a pair scenario rather than n-many pfs
        def pair_euler_totient_fun(n, pf1, pf2):
            # n * (1-(1/pfs[0])) * (1-(1/pfs[1])) ... 
            return Decimal(n) * Decimal(Decimal(1) - (Decimal(1)/pf1)) * Decimal(Decimal(1) - (Decimal(1)/pf2))
        
        # Verifies n, m are permutations of each other
        def check(n, m):
            n_str = str(n)
            m_str = str(int(m))
      
            if not len(n_str) == len(m_str):
                return False

            n_str_arr = list(n_str)
            n_str_arr.sort()
            m_str_arr = list(m_str)
            m_str_arr.sort()
 
            for x in range(0, len(n_str_arr), 1):
                if not n_str_arr[x] == m_str_arr[x]:
                    return False

            return True
       
        def solve():
            ALGO_BEGIN = time.time()

            lowest = 999_999_999
            lowest_n = 999_999_999

            L = len(PRIMES)

            '''
            From: https://projecteuler.net/about

            "I solved it by using a search engine, does that matter?

            Making use of the internet to research a problem is to be encouraged as there could be 
            hidden treasures of mathematics to be discovered beneath the surface of many of these 
            problems. However, there is a fine line between researching ideas and using the answer 
            you found on another website. If you photocopy a crossword solution then what have you 
            achieved?"

            "However, the rule about sharing solutions outside of Project Euler does not apply 
            to the first one-hundred problems, as long as any discussion clearly aims to instruct methods, 
            not just provide answers, and does not directly threaten to undermine the enjoyment of solving 
            later problems. Problems 1 to 100 provide a wealth of helpful introductory teaching material 
            and if you are able to respect our requirements, then we give permission for those problems 
            and their solutions to be discussed elsewhere."

            # We observe two things:
            ## 1. The smallest ratio will be the closest to n/phi(n) = 1
            ## 2. n and phi(n) are related in such a way when n has the fewest number of prime factors of the same rank.
            ### 2a. It's easy to prove that the smallest single to three digit primes of the same rank don't produce low ratios that are premutations.
            ### 2b. It's easy to prove that primes of different ranks don't produce low ratios that are premutations.
            ### 2c. It's time-consuming but I've tested up to 4.5 million n that any n with > 2 pfs doesn't produce low ratios that are premutations.
            ### Therefore, by induction two different pfs of the same rank will produce the lowest ratio. (And hopefully proven by deductive decideability below)

            Insight 2. is partially from the blog: https://martin-ueding.de/posts/project-euler-solution-70-totient-permutation/ which is legitimate given 
            the above Project Euler rules. I formally verify that below and with prior brute-force approaches through the first 4.5 million.

            I've customized the above using code I've used to solve other examples.
            '''

            for p1 in range(0, L, 1):
                pf1 = PRIMES[p1]
                if pf1 > 10_000:
                    break

                for p2 in range(0, L, 1):
                    if p1 == p2:
                        continue

                    pf2 = PRIMES[p2]
                    if pf2 > 10_000:
                        break

                    n = pf1 * pf2

                    # Will always increase at this point
                    if n >= 10_000_000:
                        break

                    totient = pair_euler_totient_fun(n, pf1, pf2)

                    if check(n, totient):
                        ratio = Decimal(n) / totient
                        msg(result_data, "Ratio: " + str(ratio) + " with prime factors: " + str(pf1) + " * " + str(pf2) + " = " + str(n) + " and totient: " + str(totient))
                        if ratio < lowest:
                            lowest = ratio
                            lowest_n = n
                            msg(result_data, "New lowest ratio found: " + str(ratio) + " with prime factors: " + str(pf1) + " * " + str(pf2) + " = " + str(n) + " and totient: " + str(totient))
                
            conclude(result_data, lowest_n, ALGO_BEGIN)
  
            if lowest_n == 999_999_999:
                msg(result_data, "No solution found!")

        solve() # New lowest ratio found: 1.000709051124811280540317405 with prime factors: 2339 * 3557 = 8319823 and totient: 8313928.000000000000000000000
                                         
    except Exception as ex:

        print('Exception: ' + str(ex))