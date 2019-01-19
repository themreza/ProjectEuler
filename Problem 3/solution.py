# Project Euler - Problem 3
# ----------------------------
# Description: 
#   The prime factors of 13195 are 5, 7, 13 and 29.
#   What is the largest prime factor of the number 600851475143 ?
# ----------------------------
# Plan of attack:
#   A prime number is an integer (2, 3, 5, 7, 9 ...) which is only divisible by 1 and itself.
#   Start dividing the given number by 2 and higher up to the number itself until we get a remainder of 0.
#   Add the number that divided it into the list of prime numbers.
#   Store the result of division as the new number and repeat the same process.
#   Stop the process if the current number is prime, meaning only divisible by itself (and 1 which we don't check since we start at 2).
# ----------------------------
# Solution by Mohammad Tomaraei
# ----------------------------

current_number = 600851475143
prime_factors = []

while current_number != 1: # The loop stops when the current number is 1, the result of dividing current_number prime number by itself
  for i in range(2, current_number+1): # Even though the range is defined as 2 to current_number, the actual last i is current_number-1, so we add 1
    if current_number % i == 0: # Check if current_number is divisible by i with a reminder of 0
      prime_factors.append(i) # i is a prime factor of current_number
      current_number = int(current_number / i) # Update current_number to be the result of the division
      break # Refresh the loop with the new current_number

# Display the results
print(prime_factors)