import time

def factorial(n):
  product = 1

  for i in range(2, n+1):
    product *= i  

  return product

while True:
  try: 
    n = int(input("Enter a number to find its factorial: "))
    break;
  except ValueError:
    print("Please enter a valid integer.")

before = time.perf_counter()
result = factorial(n);
after = time.perf_counter()
diff = after - before
print(f"Result: {result} \n Latency: {diff:.8f} seconds")
