# Project Euler - Problem 6
# ----------------------------
# Description: 
#   The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385.
#   The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025.
#   Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#   Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# ----------------------------
# Plan of attack:
#   Just do as the description says :)
# ----------------------------
# Solution by Mohammad Tomaraei
# ----------------------------

number_min = 1
number_max = 100
sum_of_squares = 0
square_of_sums = 0

for i in range(number_min, number_max+1): # Loop through the numbers
  sum_of_squares += i ** 2 # Sum the square of each number to sum_of_squares
  square_of_sums += i # For now, just sum each number individually in square_of_sums

square_of_sums = square_of_sums ** 2 # Square the sum of numbers

# Display the results
print(square_of_sums - sum_of_squares)

