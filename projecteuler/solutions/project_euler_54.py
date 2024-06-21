# https://projecteuler.net/problem=54
from lib import initialize, msg, conclude
import time

if __name__ == '__main__':

    try:

        result_data = initialize(54, 376, 0, 0, [])
    
        def init():
            stringData = []
            fileHandler = open('data/project_euler_54_input.txt')
            for line in fileHandler:
                stringData.append(line.replace('\n', ''))

            return stringData

        DATA = init()

        def score_hands(hands_str):
            HANDS = hands_str.split(" ")
            PLAYER_1 = HANDS[0:5]
            PLAYER_2 = HANDS[5:10]

            score_1 = hash_hand(PLAYER_1)
            score_2 = hash_hand(PLAYER_2)

            if score_1[0] > score_2[0]:
                return 1
            
            if score_2[0] > score_1[0]:
                return 2

            # Tie Breaking
            for x in range(1, len(score_1), 1):
                if score_1[x] > score_2[x]:
                    return 1
                if score_2[x] > score_1[x]:
                    return 2

        CARD_MAP = {
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            'T':10,
            'J':11,
            'Q':12,
            'K':13,
            'A':14
        }

        def hash_hand(hand):
            suits = {}
            cards = {}

            for x in range(0, len(hand), 1):
                card_str = str(hand[x])
                suit_str = card_str[len(card_str) - 1:len(card_str)]
                num_str = CARD_MAP[card_str[0:len(card_str) - 1]]
                
                suit_check = suits.get(suit_str)
                if suit_check is None:
                    suits[suit_str] = 1
                else:
                    suits[suit_str] = suits[suit_str] + 1
                
                card_check = cards.get(num_str)
                if card_check is None:
                    cards[num_str] = 1
                else:
                    cards[num_str] = cards[num_str] + 1

            SUIT_KEYS = list(suits.keys())
            CARD_KEYS = list(cards.keys())

            # Arrays
            pairs = []
            singles = []

             # Booleans only
            is_flush = len(SUIT_KEYS) == 1
            is_royal = False

            # False when False
            # Takes highest card for tie breaks when True
            is_straight = False
            is_three_kind = False
            is_four_kind = False

            for x in range(0, len(CARD_KEYS), 1):
                KEY = CARD_KEYS[x]
                VAL = cards[KEY]

                if VAL == 1:
                    singles.append(KEY)

                if VAL == 2:
                    pairs.append(KEY)

                if VAL == 3:
                    is_three_kind = KEY

                if VAL == 4:
                    is_four_kind = KEY

            singles.sort()

            if len(singles) == 5:
                is_straight = singles[4]

                for x in range(0, len(singles) - 1, 1):
                    if singles[x] == singles[x+1] - 1:
                        continue
                    else:
                        is_straight = False

                if not is_straight == False and singles[4] == 14:
                    is_royal = True

            """
            SCORE MAP:

                'High Card':        1
                'One Pair':         2
                'Two Pairs':        3
                'Three of a Kind':  4
                'Straight':         5
                'Flush':            6
                'Full House':       7
                'Four of a Kind':   8
                'Straight Flush':   9
                'Royal Flush':      10
            """

            # returns [score, tie break 1, tie break 2, tie break 3]
            pairs.sort()

            if not is_straight == False and is_flush and is_royal:
                # Royal Flush - Tie Break
                return [10, is_straight, is_straight, is_straight]

            if not is_straight == False and is_flush:
                # Straight Flush - Tie Break
                return [9, is_straight, is_straight, is_straight]

            if not is_four_kind == False and len(singles) == 1:
                # Four of Kind - Tie Break
                return [8, is_four_kind, singles[0], singles[0]]

            if not is_three_kind == False and len(pairs) == 1:
                # Full House - Tie Break
                return [7, is_three_kind, pairs[0], pairs[0]]

            if is_flush:
                # Flush - Tie Break
                return [6, is_flush, is_flush, is_flush]

            if not is_straight == False:
                # Straight - Tie Break
                return [5, is_straight, is_straight, is_straight]

            if not is_three_kind == False and len(singles) == 2:
                # Three of a Kind - Tie Break
                return [4, is_three_kind, singles[1], singles[0]]

            if len(pairs) == 2 and len(singles) == 1:
                # Two Pairs - Tie Break
                return [3, pairs[1], pairs[0], singles[0]]

            if len(pairs) == 1 and len(singles) == 3:
                # One Pair - Tie Break
                return [2, pairs[0], singles[2], singles[1]]

            if len(singles) == 5:
                # Highest Card - Tie Break
                return [1, singles[4], singles[3], singles[2]]

            raise Exception("Error: no score for hand " + str(hand) + " found!")

        def solve():
            ALGO_BEGIN = time.time()

            player_one_wins_total = 0

            for x in range(0, len(DATA), 1):
                outcome = score_hands(DATA[x])
                # msg(result_data, "Player " + str(outcome) + " wins hand!")

                if outcome == 1:
                    player_one_wins_total = player_one_wins_total + 1

            msg(result_data, "Player one won: " + str(player_one_wins_total) + " times")
            conclude(result_data, player_one_wins_total, ALGO_BEGIN)

        solve() # Player one won: 376 times

    except Exception as ex:

        print('Exception: ' + str(ex))