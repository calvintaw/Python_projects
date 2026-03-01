def b_to_d(n=1010):
  string = str(n)
  length = len(string)
  power = length - 1
  result = 0

  for i in range(length):
    if string[i] == "1":
      result += 2**power
    power -= 1
                    
  return result;


def d_to_b(n=10):
  x = n;
  string = str(n)
  length = len(string)
  binary_str_len = length * 4
  power = binary_str_len - 1
  result = ""

  for i in range(power, -1, -1):
    y = x
    divisor = 2**i
    
    if x >= divisor:
      result += "1"
      # quotient = x // divisor
      remainder = x % divisor
      x = remainder;
    else:
      result += "0" if len(result) != 0 else ""

    # print(f"power = 2^{i} = {2**i}")
    # print(f"dividend={y}, remainder: {remainder}, x = {x}, divisor = {divisor}")
    # print(f"======")

  return result


for i in range(1, 100_000, 3):
  x= d_to_b(i)
  print(i, i == b_to_d(x))

# i = 100_0000
# x = d_to_b(i)
# print(i, i == b_to_d(x))

# print(b_to_d(1101110010111011110001001101010111100) == 118505380540)
# print(d_to_b(118505380540) == 1101110010111011110001001101010111100)

# n = 12
# arr = []
# binary_str = ""
# for i in range(1, n + 1):
#   res = d_to_b(i).lstrip('0')
#   binary_str += res
#   arr.append(res)
  
# print(b_to_d(binary_str))
# print(arr)
# print("".join(arr))
# print("1101110010111011110001001101010111100")