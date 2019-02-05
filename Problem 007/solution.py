# Project Euler - Problem 7
# ----------------------------
# Description: 
#   By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#   What is the 10 001st prime number?
# ----------------------------
# Plan of attack:
#   Begin with the first prime number, 2, and check every next number until the desired nth prime number is found.
# ----------------------------
# Solution by Mohammad Tomaraei
# ----------------------------

import math

nth_prime = 10001
current_number = 2
current_prime = 0
  
# Check if a number is prime
# This is a simplified version of the algorithm explained in Problem 5
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2)) # all() returns true if all items are true

# Loop until the nth prime is discovered
while True:
  if is_prime(current_number):
    current_prime += 1
  if current_prime == nth_prime:
    break
  else:
    current_number = current_number + 1

# Display the result
print(current_number)