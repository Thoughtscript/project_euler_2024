# https://projecteuler.net/problem=836
from lib import initialize, conclude, msg
import time

if __name__ == '__main__':

    try:

        result_data = initialize(836, "aprilfoolsjoke", 0, 0, [])

        def solve():
            ALGO_BEGIN = time.time()

            result = "affine"[0]
            result += "plane"[0]
            result += "radically"[0]
            result += "integral"[0]
            result += "local"[0]
            result += "field"[0]
            result += "open"[0]
            result += "oriented"[0]
            result += "line"[0]
            result += "section"[0]
            result += "jacobian"[0]
            result += "orthogonal"[0]
            result += "kernel"[0]
            result += "embedding"[0]
            
            conclude(result_data, result, ALGO_BEGIN)

        solve() #aprilfoolsjoke

    except Exception as ex:

        print('Exception: ' + str(ex))
