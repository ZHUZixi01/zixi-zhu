"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: One whole number N typed by the user (converted to int).
# 2. Process: Loop from 1 to N, and for each number check whether it is divisible by 2 (n % 2 == 0) to decide odd or even.
# 3. Out: One line per number, saying "odd" or "even".
# 4. What happens on 0, on a negative number, on a very large number: 
# 0: say the range is empty and stop (no numbers to show).
# negative: same, say the range is empty and stop.
# 5000: ask the user to confirm first, because 5000 lines would flood the screen.


# Your code below

# Ask the user for a whole number
n = int(input("Enter a number N: "))

# Decide what to do for each edge case before looping
if n <= 0:
    # 0 or negative: nothing to show, so stop early
    print("There are no numbers from 1 to", n)
elif n > 1000:
    # very large: ask for confirmation first
    answer = input(str(n) + " lines is a lot. Continue? (yes/no): ")
    if answer.lower() != "yes":
        print("Stopped.")
    else:
        # loop from 1 to N and check each number
        for i in range(1, n + 1):
            if i % 2 == 0:
                print(i, "is even")
            else:
                print(i, "is odd")
else:
    # normal case: loop from 1 to N
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")
