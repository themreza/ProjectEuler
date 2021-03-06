# Project Euler - Problem 2
# ----------------------------
# Description: 
#   Each new term in the Fibonacci sequence is generated by adding the previous two terms.
#   By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#   By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
# ----------------------------
# Plan of attack:
#   We begin generating Fibonacci numbers as great as 4 million. Each time we generate a new number, we check if the number is even.
#   By the time we reach the last number, we should have our sum completed.
# ----------------------------
# Solution by Mohammad Tomaraei
# ----------------------------

current_number, previous_number = 1, 1 # Starting at 1, the previous term is also 1
sum_of_even_numbers = 0

while current_number <= 4000000: # Go all the way to 4 million
  if current_number % 2 == 0: # Check if the current number is even
    sum_of_even_numbers += current_number # Add the current number of the total sum
  # We're using multiple assignment to prevent the need of creating a temporary variable to update previous_number
  current_number, previous_number = current_number + previous_number, current_number # Generate the next Fibonacci number, and update the previous number

# Display the total sum of even numbers
print(sum_of_even_numbers)