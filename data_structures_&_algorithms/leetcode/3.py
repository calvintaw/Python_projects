# Link: https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        n = len(s)
        i = 0
        sum = 0

        rule = {
          "I": {"V", "X"},
          "X": {"L", "C"},
          "C": {"D", "M"},
        }

        while i < n:
            if i + 1 < n and s[i] in rule and s[i+1] in rule[s[i]]:
                sum += roman[s[i] + s[i+1]]
                i += 2
                continue

            sum += roman[s[i]]
            i += 1

        return sum


# -----------------------------
# Testing template
# -----------------------------/

solution = Solution()

test_cases = [
    ("III", 3),       # I + I + I = 3
    ("L", 50),       # I + I + I = 3
    ("LVIII", 58),
    ("DCXXI", 621),    # L + V + I + I + I = 50 + 5 + 3 = 58
    ("MCMXCIV", 1994) # M + CM + XC + IV = 1000 + 900 + 90 + 4 = 1994
]

for s, expected in test_cases:
    print(f"\nTesting input: {s}")
    result = solution.romanToInt(s)
    print(f"Result: {result}, Expected: {expected}, {"Pass" if result == expected else "Fail"}")