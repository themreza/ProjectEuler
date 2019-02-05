# Project Euler - Problem 10
# ----------------------------
# Description: 
#   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#   Find the sum of all the primes below two million.
# ----------------------------
# Plan of attack:
#   The main focus of this assignment is the primality test algorithm.
#   Currently we use an algorithm that takes about 20 seconds to test primes under two million.
#   We loop through numbers from 2 (smallest prime) all the way to the target number and check for primes. 
# ----------------------------
# Solution by Mohammad Tomaraei
# ----------------------------

import math
import time

target_number = 2000000
total_sum = 0

start = time.time() # Time the solution

# Check if a number is prime
# This is a simplified version of the algorithm explained in Problem 5
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2)) # all() returns true if all items are true

# Loop through the numbers
for i in range(2, target_number+1):
  if is_prime(i):
    total_sum += i

end = time.time()
print(total_sum)
print("This program took", end - start, "seconds to finish.")