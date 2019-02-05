# Project Euler - Problem 4
# ----------------------------
# Description: 
#   A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#   Find the largest palindrome made from the product of two 3-digit numbers.
# ----------------------------
# Plan of attack:
#   Define the largest and smallest n-digit numbers possible. Begin two nested loops with the outer loop starting from the largest n-digit
#   number down to the smallest n-digit number, and the inner loop starting from the current number in the outer loop and going down to the
#   smallest n-digit number. Check for a palindrome every time we step through the loops and skip products that are smaller than the last
#   found palindrome. Report the largest palindrome found.
# ----------------------------
# Solution by Mohammad Tomaraei
# ----------------------------

n_digits = 3
max_number, min_number = 0, 1
largest_palindrome = 0
    
# Add n many nines to create the largest n-digit number possible
for n in range(n_digits):
  max_number = (max_number * 10) + 9

# Add n many zeros to make the smallest n-digit number possible
for n in range(n_digits-1):
  min_number = min_number * 10

# Palindrome check
def palindrome_check(a, b):
  if str(a * b) == str(a * b)[::-1]: # We can convert the number into a string array of digits and check it with its reversed array
    return 1
  return 0
  
# Loop through possibilities and check for a palindrome
for a in range(max_number, min_number-1, -1): 
  for b in range(a, min_number-1,-1): 
    if a*b < largest_palindrome: # Skip checking numbers that are smaller than the last found palindrome
      break
    if palindrome_check(a,b):
      largest_palindrome = a*b # Update the largest palindrome number

# Display the results
print(largest_palindrome)
      