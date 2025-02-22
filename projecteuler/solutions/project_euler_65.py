# https://projecteuler.net/problem=65
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    try:   

        result_data = initialize(65, 272, 0, 0, [])

        # Note: The first 100 Euler Decimal Expansions were 
        # apparently first published by Glaisher 1871!

        # So apparently continued fraction expansion for e has no apparent pattern, 
        # implying it'll have to computed.

        # Instead I will the OEIS A003417 Sequence... adjusted slightly for the problem
        ## https://oeis.org/A003417

        e_c_f = [
         1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 
         8, 1, 1, 10, 1, 1, 12, 1, 1, 14,
         1, 1, 16, 1, 1, 18, 1, 1, 20, 1,
         1, 22, 1, 1, 24, 1, 1, 26, 1, 1,
         28, 1, 1, 30, 1, 1, 32, 1, 1, 34, 
         1, 1, 36, 1, 1, 38, 1, 1, 40, 1,
         1, 42, 1, 1, 44, 1, 1, 46, 1, 1,
         48, 1, 1, 50, 1, 1, 52, 1, 1, 54,
         1, 1, 56, 1, 1, 58, 1, 1, 60, 1,
         1, 62, 1, 1, 64, 1, 1, 66, 
         
         # Adding these
         1, 1, 68
        ]

        '''
        Looks like subsequences of (x, 1, 1, x + 2) if more are needed!

        Doesn't seem like any are (x, y) they are always separated (1, 1)...

        So, at most one e_c_f > 1 multiple in each computation... (? below will always 1)
        '''

        print(len(e_c_f))

        def solve():
            ALGO_BEGIN = time.time()

            '''
            Observe that for any i in convergents:

            num_k               num_(k - 1) * e_c_f(k-1)  + num_(k -2) * ? 
            -------     =       -------------------------------------
            denom_k             ...
            
            denom doesn't appear to play any role in the calculation of the num.

            e.g. - 

            1    2    1    1    4    1      1      6

            2    3    8    11   19   87    106   193   1264
            -    -    -    -    -    -     -     -     -
            1    1    3    4    7    32    39    71    465
            '''

            conv_nums = [2, 3, 8, 11]

            while (len(conv_nums) < 100):
                I = len(conv_nums)
                K_1 = conv_nums[I - 1]
                K_2 = conv_nums[I - 2]
                E = e_c_f[I-1]
                computed = K_1 * E + K_2
                conv_nums.append(computed)
                msg(result_data, "Computed Convergent found: " + str(computed))
            
            msg(result_data, "Computed Convergents: " + str(conv_nums))

            hundreth_convergent = str(conv_nums[99])
            msg(result_data, "One Hundreth Convergent Numerator found: " + hundreth_convergent)

            result = 0

            for n in range(0, len(hundreth_convergent), 1):
                result += int(hundreth_convergent[n])
           
            msg(result_data, "Sum of One Hundreth Convergent Numerator is " + str(result))
            conclude(result_data, result, ALGO_BEGIN)
                  
        solve()

    except Exception as ex:

        print('Exception: ' + str(ex))
