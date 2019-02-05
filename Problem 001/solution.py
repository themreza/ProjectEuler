# Project Euler - Problem 1
# ----------------------------
# Description: 
#   If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#   The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
# ----------------------------
# Plan of attack:
#   Since we're looking for multiples of 3 or 5, we have to find the set of unique numbers that belong
#   to the sets of multiples of 3 and multiples of 5. Then we can calculate the sum of numbers in this set.
# ----------------------------
# Solution by Mohammad Tomaraei
# ----------------------------

# Set (list) of numbers
number_set = []

# Loop through all numbers from 1 to 1000
for i in range (1,1000):
  # Check if the current number is divisible by 3 or 5
  if (i % 3 == 0) or (i % 5 == 0):
    number_set.append(i)

# Remove duplicate numbers
number_set = list(set(number_set))

# Diplay the sum of numbers in number_set
print(sum(number_set))