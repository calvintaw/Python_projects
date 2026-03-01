#link: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/solutions/?envType=daily-question&envId=2026-02-28


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # My solution
        # ===================

        # def b_to_d(n):
            
        #     string = str(n)
        #     length = len(string)
        #     power = length - 1
        #     result = 0

        #     for i in range(length):
        #         if string[i] == "1":
        #             result += 2 ** power
        #         power -= 1

        #     return result % (10**9+7)

        # def d_to_b(n):
        #     x = n
        #     string = str(n)
        #     length = len(string)
        #     binary_str_len = length * 4
        #     power = binary_str_len - 1
        #     result = ""

        #     for i in range(power, -1, -1):
        #         divisor = 2 ** i

        #         if x >= divisor:
        #             result += "1"
        #             remainder = x % divisor
        #             x = remainder
        #         else:
        #             result += "0" if len(result) != 0 else ""

        #     return result

        # binary_str = ""

        # for i in range(1, n + 1):
        #     binary_str += d_to_b(i)

        # return b_to_d(binary_str)


        # Intended Solution
        # ===================
        length = 0
        result = 0

        for i in range(1, n+1):
            if (i & (i - 1) == 0):
                length += 1
            
            result = ((result << length) | i) % (10**9+7)

        return result


# ===== Test Setup =====

def run_test(n):
    ans = Solution().concatenatedBinary(n)
    print(f"n = {n} -> {ans}")

# ===== Test Case 1 =====
run_test(1)      # Expected Output: 1

# ===== Test Case 2 =====
run_test(3)      # Expected Output: 27

# ===== Test Case 3 =====
run_test(12)     # Expected Output: 505379714