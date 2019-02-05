# Project Euler - Problem 5
# ----------------------------
# Description: 
#   2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#   What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# ----------------------------
# Plan of attack:
#   2520 is 2*2*2*3*3*5*7. In other words, it is the least common multiple (LCM) of numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10.
#   Find the LCM of the given range of numbers through prime factorization and multiply them together to get the desired number.
# ----------------------------
# Solution by Mohammad Tomaraei
# ----------------------------

import math
import collections

factor_min = 1
factor_max = 20
parent_lcm = collections.defaultdict(int) # This is an associative array that holds the largest power of LCM numbers found below
final_answer = 1

# Loop through the given range of numbers one by one
for i in range(factor_min, factor_max+1):
  lcm = [] # Initiate an empty lcm list
  if i > 1: # Ignore 1 as it is a common multiple of all numbers
    # Prime factorization
    while i % 2 == 0: # Check if the number is divisible by 2
      lcm.append(2) # Add 2 to the LCM list
      i = i / 2 # Update the current number
    for j in range(3,int(math.sqrt(i))+1,2): # Loop through the odd numbers 3, 5, 7, etc. until sqrt(i).
      while i % j == 0: # Check if the number is divisible by 3, 5, 7, etc.
        lcm.append(int(j)) # Add the factor to the LCM list
        i = i / j # Update the current number
    if i > 2: # If i is a prime number greater than 2
      lcm.append(int(i)) # Add the factor to the LCM list
  counter = collections.Counter(lcm) # Using the Collections library we can find the frequency (power) of each factor
  for key, value in counter.items(): # Add the powers to the parent_lcm dictionary
    if value > parent_lcm[key]: # Check if the power of the number found is larger than the largest recorded power
      parent_lcm[key] = value # Update parent_lcm

# Print the result by raising each number to its power and multiplying them together
for number, power in parent_lcm.items():
  final_answer *= int(number ** power) # ** is the power operator in Python

print(final_answer)