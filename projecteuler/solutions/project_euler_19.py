# https://projecteuler.net/problem=19
from lib import initialize, msg, conclude, sum_list
import time
import datetime

if __name__ == '__main__':

    try:

        result_data = initialize(19, 171, 0, 0, [])

        def is_leap_year(year):
            if not year % 4 == 0:
                return False

            if year % 100 == 0 and not year % 400 == 0:
                return False

            return (year % 4 == 0 and year % 400 == 0)

        #print(is_leap_year(2000))
        #print(is_leap_year(2400))
        #print(is_leap_year(1800))
        #print(is_leap_year(1900))
        #print(is_leap_year(2200))

        # Iterate Months
        # Check if 1st of Month is a Sunday

        # Iterate Years
        # Between 1/1/1901 to 12/31/2000

        def solve():
            ALGO_BEGIN = time.time()

            count = 0
            for year in range(1901,2001,1):
                for month in range(1,13,1):
                    d = datetime.datetime(year, month, 1)
                    if d.strftime('%A') == 'Sunday':
                        count = count + 1
                        msg(result_data, "Found: " + str(d) + " is a " + d.strftime('%A'))
            
            conclude(result_data, count, ALGO_BEGIN)

        solve()

    except Exception as ex:

        print('Exception: ' + str(ex))