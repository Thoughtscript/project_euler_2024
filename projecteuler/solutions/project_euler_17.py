# https://projecteuler.net/problem=17
# For hyphens: https://www.codewars.com/kata/52724507b149fa120600031d
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    try:

        result_data = initialize(17, 21124, 0, 0, [])

        N = {
            "0": "",
            "1": "One",
            "2": "Two",
            "3": "Three",
            "4": "Four",
            "5": "Five",
            "6": "Six",
            "7": "Seven",
            "8": "Eight",
            "9": "Nine"
        }

        TENS = {
            "0": "",
            "2": "Twenty",
            "3": "Thirty",
            "4": "Forty",
            "5": "Fifty",
            "6": "Sixty",
            "7": "Seventy",
            "8": "Eighty",
            "9": "Ninety"
        }

        TEENS = {
            "10": "Ten",
            "11": "Eleven",
            "12": "Twelve",
            "13": "Thirteen",
            "14": "Fourteen",
            "15": "Fifteen",
            "16": "Sixteen",
            "17": "Seventeen",
            "18": "Eighteen",
            "19": "Nineteen"
        }

        def rmvPlaces(s):
            r = s.split()
            count = 0

            if len(r) > 3:
                for i in range(0, len(r) - 1):
                    R1 = r[i]
                    R2 = r[i+1]

                    if R1 == "Thousand":
                        if R2 == "Hundred":
                            count = count + 1
                            for j in range(i+1, len(r)):
                                r[j] = r[j+1]
                            i = 0
                        else:
                            i = i+1

                    elif R1 == "Hundred":
                        if R2 == "Hundred":
                            for j in range(i+1, len(r)):
                                r[j] = r[j+1]
                            i = 0
                        else:
                            i = i+1
                    
                    i = i+1

            RE = r[len(r)-1]
            RSE = r[len(r)-2]

            if RSE == "Thousand":
                if RE == "Hundred" or RE == "Thousand":
                    count = count + 1

            elif RSE == "Hundred":
                if RE == "Hundred" or RE == "Thousand":
                    count = count + 1

            while count > 0:
                r.pop()
                count = count - 1

            return " ".join(r).strip(" ")

        def rmv(s):
            if len(s) == 1 and s[0] == " ":
                return ""
            return s.strip(" ")

        def prepend(c, s):
            s = rmv(s)
            c = rmv(c)

            if len(s) > 0:
                 s = str(c) + " " + str(s)
            else:
                s = str(c)

            return rmv(s)

        def make_num(num):
            if num == 0:
                return "Zero"

            S = str(num)
            # P = math.ceil(len(S) / 3)
            s = ""
            p = 1
            i = len(S) - 1
            c = 1

            while i >= 0:
                ch = S[i]
                t = ""

                if c == 1:
                    t = str(ch)

                    if i == 0 and c > 0:
                        s = prepend(str(N[ch]), s)

                    if i > 0:
                        t = str(S[i-1]) + str(t)
                        if TEENS.get(t) is not None:
                            s = prepend(str(TEENS[t]), s)
                        else:
                            s = prepend(str(TENS[S[i-1]]) + " " + str(N[ch]), s)
                        i = i-1
                        c = c+1
                
                if c == 3:
                    s = prepend(str(N[ch]) + " Hundred", s)

                    if i > 0:
                        if p == 1:
                            s = prepend("Thousand", s)
                            p = p+1

                c = c+1
                if c > 3:
                    c = 1
                i = i-1

            RESULT = rmvPlaces(s)
            return RESULT

        # Makes all numbers like Seven Hundred Sixty, Nine, etc.
        def make_nums():
            nums = []

            for x in range(1,1001,1):
                nums.append(make_num(x))

            return nums

        # 901 numbers at 100 or above. 
        # 10 lack any "tens" spot: 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000.
        # The rest are like: 101, 110, 229, etc.
        # So, (901 - 10) * 3 is the total value to add: 2,673 if all those numbers include 'and'.

        # (901- 10 - 80) * 3 if 101, 108, 308, etc. lack 'and' - unclear.

        def solve():
            ALGO_BEGIN = time.time()

            count = 0

            nums = make_nums()

            for x in range(0, len(nums), 1):
                line = nums[x]
                line = line.replace(" ", "")
                line = line.replace("\n", "")
                count += len(line)
                # msg(result_data, line + " " + str(len(line)))

            msg(result_data, "Adding " + str(2673) + " for 'and's")
            conclude(result_data, count + 2673, ALGO_BEGIN)

        solve() # 21124

    except Exception as ex:
        print('Exception: ' + str(ex))