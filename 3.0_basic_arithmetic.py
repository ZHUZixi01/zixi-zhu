"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Two numbers from the user (text converted to float).
# 2. Process: Add, subtract, multiply and divide them. Check for zero before dividing.
# 3. Out: The sum, difference, product and division. If the second number is zero, show a message instead.
# 4. What happens when the second number is zero, and why:  
# I show a message and don't divide, because dividing by zero would crash the program (ZeroDivisionError).


# Your code below
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

# add the two numbers
sum = num1 + num2

# print the sum
print("The sum of two numbers is:", sum)

# finding the difference between two numbers
diff = num1 - num2
print("The difference between two numbers is:", diff)

# finding the product of two numbers
product = num1 * num2
print("The product of two numbers is:", product)

# finding the division of two numbers
if num2 !=0:
    division = num1 / num2
    print("The divison of two numbers is", division)
else:
    print("The number 2 is zero")