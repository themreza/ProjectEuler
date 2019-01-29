# Project Euler - Problem 9
# ----------------------------
# Description: 
#   A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2.
#   For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2. There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#   Find the product abc.
# ----------------------------
# Plan of attack:
#   We start by calculating the upper bounds for a and b, and then count backward from these upper bounds, trying every triplet
#   possible. If we find a pair with the specified target sum and matching the Pythagorean theorem, we will print the result and stop the routine.
# ----------------------------
# Solution by Mohammad Tomaraei
# ----------------------------

from math import floor
import time

start = time.time() # Time the solution
target_sum = 1000
a_upper_bound = int(floor(target_sum/3)) # This will return 333, but in reality it should be 332. We don't subtract 1 because the loop below does it.
b_upper_bound = int(floor(target_sum/2)) # The same idea happens here too.

# We will count backwards from the upper bounds to make the program more efficient
for a in range(a_upper_bound, 1, -1):
  for b in range(b_upper_bound, a+1, -1):
    for c in range((target_sum - a - b + 1), b+1, -1):
      if a+b+c == target_sum and a**2 + b**2 == c**2:
        # Display the results
        output = "The Pythagorean triplet %r, %r, %r has the product %r." % (a, b, c, a*b*c)
        print(output)
        end = time.time()
        quit()
      