import argparse
from solutions import lib

if __name__ == '__main__':

    try:

        parser = argparse.ArgumentParser()
        parser.add_argument('--max_num')  
        args = parser.parse_args()

        print("Arguments received for _make_and_print_fib.py: [ max_num: " + str(args.max_num) + " ]")

        '''
        FIB. NO. HELPERS
        '''
        def make_fib_nos(max_num, do_print = False):
            fibs = [0,1]

            while(fibs[len(fibs) - 1] < max_num):
                next_fib = fibs[len(fibs) - 1] + fibs[len(fibs) - 2]
                fibs.append(next_fib)

            if do_print:
                print(fibs)

            return fibs
        
        def make_and_print(max_num):
            fibs_arr = make_fib_nos(max_num, False)
            fibs_arr_file = open('solutions/data/fib_nos_to_' + str(max_num) + '_arr.py', 'w')
            fibs_arr_file.write("fibs=" + str(fibs_arr)) # Make it easy to load
            fibs_arr_file.close()

            fibs_map = lib.list_to_map(fibs_arr, False)
            fibs_map_file = open('solutions/data/fib_nos_to_' + str(max_num) + '_map.py', 'w')
            fibs_map_file.write("fibs=" + str(fibs_map)) # Make it easy to load
            fibs_map_file.close()

        make_and_print(int(args.max_num))

    except Exception as ex:

        print('Exception: ' + str(ex))