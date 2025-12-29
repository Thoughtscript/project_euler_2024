# https://projecteuler.net/problem=836
from lib import initialize, conclude, msg
import time

if __name__ == '__main__':

    try:
        ALGO_BEGIN = time.time()
        result_data = initialize(836, "aprilfoolsjoke", 0, 0, [])
        conclude(result_data, "aprilfoolsjoke", ALGO_BEGIN)

    except Exception as ex:

        print('Exception: ' + str(ex))
