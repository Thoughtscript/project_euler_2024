# https://projecteuler.net/problem=125
from lib import initialize, conclude, msg, sum_list
import time

'''
100 000 000 - max length 9 palindrome string
'''

if __name__ == '__main__':

    try:

        result_data = initialize(125, 2906969179, 0, 0, [])

        # cached = []

        def generate_all_odd_palindromes_of_length(n):
            last_array = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            counter = 1

            while counter < n:
                temp = []
                for x in range(0, len(last_array), 1):
                    for y in range(0, 10, 1):
                        temp.append(str(y) + str(last_array[x]) + str(y))
                last_array = temp
                counter += 2

            return last_array

        # YAAY -> Y AA Y
        # YA - AY
        # These are identical
        def generate_all_even_palindromes_of_length(n):
            last_array = ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99"]
            counter = 2

            while counter < n:
                temp = []
                for x in range(0, len(last_array), 1):
                    for y in range(0, 10, 1):
                        temp.append(str(y) + str(last_array[x]) + str(y))
                last_array = temp
                counter += 2

            return last_array

        def check_cons_square(num_str, max_num):
            if num_str[0] == "0":
                return 0
            
            num_num = int(num_str)
            if num_num >= max_num:
                return 0

            for x in range(1, num_num, 1):
                total = 0
                squares = []
                if pow(x, 2) > num_num:
                    break

                for y in range(x, num_num, 1):
                    total += pow(y, 2)
                    squares.append(y)
                    if total > num_num:
                        break

                    if total == num_num and len(squares) > 1:
                        msg(result_data, "Palindromic Consecutive square found: " + num_str)
                        # cached.append(num_num)
                        return num_num
            return 0

        def find_palindromic_cons_squares(max_num):
            ALGO_BEGIN = time.time()

            num_str = str(max_num)
            total = 0
            pals =  ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99"] + ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for x in range(3, len(num_str) + 1, 1):
                if x % 2 == 0:
                    pals = pals + generate_all_even_palindromes_of_length(x)
                else:
                    pals = pals + generate_all_odd_palindromes_of_length(x)

            for x in range(0, len(pals), 1):
                total += check_cons_square(pals[x], max_num)

            conclude(result_data, total, ALGO_BEGIN)
            # print(cached)

        # find_palindromic_cons_squares(100_000_000) # 2906969179

        '''
        "Palindromic Consecutive square found: 55",
        "Palindromic Consecutive square found: 77",
        "Palindromic Consecutive square found: 5",
        "Palindromic Consecutive square found: 505",
        "Palindromic Consecutive square found: 313",
        "Palindromic Consecutive square found: 818",
        "Palindromic Consecutive square found: 434",
        "Palindromic Consecutive square found: 636",
        "Palindromic Consecutive square found: 545",
        "Palindromic Consecutive square found: 181",
        "Palindromic Consecutive square found: 595",
        "Palindromic Consecutive square found: 1001",
        "Palindromic Consecutive square found: 1111",
        "Palindromic Consecutive square found: 4334",
        "Palindromic Consecutive square found: 1441",
        "Palindromic Consecutive square found: 6446",
        "Palindromic Consecutive square found: 1771",
        "Palindromic Consecutive square found: 51015",
        "Palindromic Consecutive square found: 99199",
        "Palindromic Consecutive square found: 41214",
        "Palindromic Consecutive square found: 17371",
        "Palindromic Consecutive square found: 44444",
        "Palindromic Consecutive square found: 46564",
        "Palindromic Consecutive square found: 97679",
        "Palindromic Consecutive square found: 19691",
        "Palindromic Consecutive square found: 21712",
        "Palindromic Consecutive square found: 65756",
        "Palindromic Consecutive square found: 81818",
        "Palindromic Consecutive square found: 17871",
        "Palindromic Consecutive square found: 42924",
        "Palindromic Consecutive square found: 161161",
        "Palindromic Consecutive square found: 171171",
        "Palindromic Consecutive square found: 981189",
        "Palindromic Consecutive square found: 191191",
        "Palindromic Consecutive square found: 972279",
        "Palindromic Consecutive square found: 982289",
        "Palindromic Consecutive square found: 923329",
        "Palindromic Consecutive square found: 363363",
        "Palindromic Consecutive square found: 904409",
        "Palindromic Consecutive square found: 444444",
        "Palindromic Consecutive square found: 944449",
        "Palindromic Consecutive square found: 554455",
        "Palindromic Consecutive square found: 964469",
        "Palindromic Consecutive square found: 494494",
        "Palindromic Consecutive square found: 525525",
        "Palindromic Consecutive square found: 435534",
        "Palindromic Consecutive square found: 635536",
        "Palindromic Consecutive square found: 485584",
        "Palindromic Consecutive square found: 646646",
        "Palindromic Consecutive square found: 656656",
        "Palindromic Consecutive square found: 166661",
        "Palindromic Consecutive square found: 127721",
        "Palindromic Consecutive square found: 137731",
        "Palindromic Consecutive square found: 108801",
        "Palindromic Consecutive square found: 138831",
        "Palindromic Consecutive square found: 148841",
        "Palindromic Consecutive square found: 188881",
        "Palindromic Consecutive square found: 629926",
        "Palindromic Consecutive square found: 139931",
        "Palindromic Consecutive square found: 9940499",
        "Palindromic Consecutive square found: 6780876",
        "Palindromic Consecutive square found: 5090905",
        "Palindromic Consecutive square found: 1690961",
        "Palindromic Consecutive square found: 4211124",
        "Palindromic Consecutive square found: 6831386",
        "Palindromic Consecutive square found: 9051509",
        "Palindromic Consecutive square found: 1681861",
        "Palindromic Consecutive square found: 3242423",
        "Palindromic Consecutive square found: 3162613",
        "Palindromic Consecutive square found: 9072709",
        "Palindromic Consecutive square found: 1972791",
        "Palindromic Consecutive square found: 1992991",
        "Palindromic Consecutive square found: 5603065",
        "Palindromic Consecutive square found: 9313139",
        "Palindromic Consecutive square found: 6523256",
        "Palindromic Consecutive square found: 9343439",
        "Palindromic Consecutive square found: 6843486",
        "Palindromic Consecutive square found: 9563659",
        "Palindromic Consecutive square found: 9793979",
        "Palindromic Consecutive square found: 2904092",
        "Palindromic Consecutive square found: 9814189",
        "Palindromic Consecutive square found: 1224221",
        "Palindromic Consecutive square found: 4424244",
        "Palindromic Consecutive square found: 8424248",
        "Palindromic Consecutive square found: 5824285",
        "Palindromic Consecutive square found: 9334339",
        "Palindromic Consecutive square found: 6844486",
        "Palindromic Consecutive square found: 9105019",
        "Palindromic Consecutive square found: 3015103",
        "Palindromic Consecutive square found: 9435349",
        "Palindromic Consecutive square found: 7355537",
        "Palindromic Consecutive square found: 1365631",
        "Palindromic Consecutive square found: 6106016",
        "Palindromic Consecutive square found: 5536355",
        "Palindromic Consecutive square found: 6546456",
        "Palindromic Consecutive square found: 2176712",
        "Palindromic Consecutive square found: 5276725",
        "Palindromic Consecutive square found: 4776774",
        "Palindromic Consecutive square found: 5367635",
        "Palindromic Consecutive square found: 1077701",
        "Palindromic Consecutive square found: 6277726",
        "Palindromic Consecutive square found: 3187813",
        "Palindromic Consecutive square found: 5718175",
        "Palindromic Consecutive square found: 3628263",
        "Palindromic Consecutive square found: 4338334",
        "Palindromic Consecutive square found: 9838389",
        "Palindromic Consecutive square found: 5258525",
        "Palindromic Consecutive square found: 5588855",
        "Palindromic Consecutive square found: 1949491",
        "Palindromic Consecutive square found: 5479745",
        "Palindromic Consecutive square found: 11600611",
        "Palindromic Consecutive square found: 92800829",
        "Palindromic Consecutive square found: 56800865",
        "Palindromic Consecutive square found: 40211204",
        "Palindromic Consecutive square found: 53211235",
        "Palindromic Consecutive square found: 32611623",
        "Palindromic Consecutive square found: 10711701",
        "Palindromic Consecutive square found: 11122111",
        "Palindromic Consecutive square found: 18422481",
        "Palindromic Consecutive square found: 47622674",
        "Palindromic Consecutive square found: 52722725",
        "Palindromic Consecutive square found: 56722765",
        "Palindromic Consecutive square found: 69722796",
        "Palindromic Consecutive square found: 15822851",
        "Palindromic Consecutive square found: 11922911",
        "Palindromic Consecutive square found: 13922931",
        "Palindromic Consecutive square found: 67233276",
        "Palindromic Consecutive square found: 46433464",
        "Palindromic Consecutive square found: 37533573",
        "Palindromic Consecutive square found: 64633646",
        "Palindromic Consecutive square found: 53933935",
        "Palindromic Consecutive square found: 69933996",
        "Palindromic Consecutive square found: 50244205",
        "Palindromic Consecutive square found: 18244281",
        "Palindromic Consecutive square found: 32344323",
        "Palindromic Consecutive square found: 52344325",
        "Palindromic Consecutive square found: 55344355",
        "Palindromic Consecutive square found: 95544559",
        "Palindromic Consecutive square found: 26744762",
        "Palindromic Consecutive square found: 63844836",
        "Palindromic Consecutive square found: 52155125",
        "Palindromic Consecutive square found: 45555554",
        "Palindromic Consecutive square found: 45755754",
        "Palindromic Consecutive square found: 16755761",
        "Palindromic Consecutive square found: 16955961",
        "Palindromic Consecutive square found: 49066094",
        "Palindromic Consecutive square found: 53166135",
        "Palindromic Consecutive square found: 44366344",
        "Palindromic Consecutive square found: 58366385",
        "Palindromic Consecutive square found: 63866836",
        "Palindromic Consecutive square found: 95177159",
        "Palindromic Consecutive square found: 34277243",
        "Palindromic Consecutive square found: 41577514",
        "Palindromic Consecutive square found: 69388396",
        "Palindromic Consecutive square found: 51488415",
        "Palindromic Consecutive square found: 17488471",
        "Palindromic Consecutive square found: 57488475",
        "Palindromic Consecutive square found: 68688686",
        "Palindromic Consecutive square found: 12888821",
        "Palindromic Consecutive square found: 62988926",
        "Palindromic Consecutive square found: 72299227",
        "Palindromic Consecutive square found: 97299279",
        "Palindromic Consecutive square found: 16399361",
        "Palindromic Consecutive square found: 43699634",
        "Palindromic Consecutive square found: 18699681",
        "Palindromic Consecutive square found: 66999966",
        '''

        def solve():
            ALGO_BEGIN = time.time()

            generated_palindromic_cons_squares = [55, 77, 5, 505, 313, 818, 434, 636, 545, 181, 595, 1001, 1111, 4334, 1441, 6446, 1771, 51015, 99199, 41214, 17371, 44444, 46564, 97679, 19691, 21712, 65756, 81818, 17871, 42924, 161161, 171171, 981189, 191191, 972279, 982289, 923329, 363363, 904409, 444444, 944449, 554455, 964469, 494494, 525525, 435534, 635536, 485584, 646646, 656656, 166661, 127721, 137731, 108801, 138831, 148841, 188881, 629926, 139931, 9940499, 6780876, 5090905, 1690961, 4211124, 6831386, 9051509, 1681861, 3242423, 3162613, 9072709, 1972791, 1992991, 5603065, 9313139, 6523256, 9343439, 6843486, 9563659, 9793979, 2904092, 9814189, 1224221, 4424244, 8424248, 5824285, 9334339, 6844486, 9105019, 3015103, 9435349, 7355537, 1365631, 6106016, 5536355, 6546456, 2176712, 5276725, 4776774, 5367635, 1077701, 6277726, 3187813, 5718175, 3628263, 4338334, 9838389, 5258525, 5588855, 1949491, 5479745, 11600611, 92800829, 56800865, 40211204, 53211235, 32611623, 10711701, 11122111, 18422481, 47622674, 52722725, 56722765, 69722796, 15822851, 11922911, 13922931, 67233276, 46433464, 37533573, 64633646, 53933935, 69933996, 50244205, 18244281, 32344323, 52344325, 55344355, 95544559, 26744762, 63844836, 52155125, 45555554, 45755754, 16755761, 16955961, 49066094, 53166135, 44366344, 58366385, 63866836, 95177159, 34277243, 41577514, 69388396, 51488415, 17488471, 57488475, 68688686, 12888821, 62988926, 72299227, 97299279, 16399361, 43699634, 18699681, 66999966]
            sum = sum_list(generated_palindromic_cons_squares)

            conclude(result_data, sum, ALGO_BEGIN)

        solve()

    except Exception as ex:

        print('Exception: ' + str(ex))