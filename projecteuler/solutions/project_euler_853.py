# https://projecteuler.net/problem=853
from lib import initialize, conclude, correct_path_and_name, load_json_file
import time, json, os

# https://oeis.org/A001175 <- This one.
if __name__ == '__main__':

    try:
        result_data = initialize(853, 44511058204, 0, 0, [])

        PRE_COMPUTED_FP = correct_path_and_name('project_euler_853_data')

        '''
        See: https://oeis.org/A001175
        '''
        def found_new_cycle(seqA, seqB, current):       
            if current < 4:
                return False
                        
            return seqA == 0 and seqB == 1
        
        def π(n):
            # From: https://en.wikipedia.org/wiki/Pisano_period#Number_of_zeros_in_the_cycle
            ## Every Pisano sequence starts with 0,1

            if n < 3:
                if n == 1:
                    return 1
        
                if n == 2:
                    return 3
            
            current = 0 # Use this so don't have to use Hexadecimal cipher 
                        ## by comparing len(seq)
                        ## offset by 2
    
            seqA, seqB = 0,1 # Use int vals not string, dict, or list

            # Interestingly, there are always 2 zeroes for 120 pisano no. sequences 
            # zero_counter = 0
 
            while (not found_new_cycle(seqA, seqB, current)):
                f = seqA + seqB
                seqA = seqB
                seqB = f % n
                current += 1
                #if seqB == 0:
                #    zero_counter +=1
                
                # Little optimization here - don't compute just get 120 or less!!!
                ## computing first 25_000 goes from: 19.330507516860962
                ## to: 0.31812000274658203
                if current > 120:
                    return 0
            
            return current
        
        def pre_compute():
            if not os.path.exists(PRE_COMPUTED_FP + '.json'):
                PRE_COMPUTED_BEGIN = time.time()
                valid_pisano_nums = []

                for n in range(1, 1_000_000_000, 1):                
                    if π(n) == 120:
                        valid_pisano_nums.append(n)

                print("Total valid_nums precomputed: " + str(len(valid_pisano_nums)) + " in " + str(time.time() - PRE_COMPUTED_BEGIN))
                project_euler_853_file = open(PRE_COMPUTED_FP + '.json', 'w')
                project_euler_853_file.write(json.dumps(valid_pisano_nums, indent=4))
                project_euler_853_file.close()

        pre_compute()

        def solve():
            ALGO_BEGIN = time.time()
            solution = 0
            precomputed = load_json_file(PRE_COMPUTED_FP)
  
            for n in range(0, len(precomputed), 1):
                solution += precomputed[n]

            conclude(result_data, solution, ALGO_BEGIN) 

        solve()

    except Exception as ex:

        print('Exception: ' + str(ex))
