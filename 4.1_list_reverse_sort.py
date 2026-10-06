"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The list I built in exercise 4.0 (no new user input).
# 2. Process: Show the list in four different orders using slicing and sorted(), then display the original list again to prove it is unchanged.
# 3. Out: The list in four orders, plus the original list at the end.
# 4. My four orders, and which ones modify the original:
# my_list[::-1] -> reversed, does NOT modify the original
# sorted(my_list) -> ascending, does NOT modify the original
# sorted(my_list, reverse=True) -> descending, does NOT modify the original
# my_list[::-1][::-1] -> back to original order, does NOT modify
# None of my four orders change the original.


# Your code below
# This is the list from exercise 4.0
my_list = [5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7]

# Order 1: reversed, using slicing -> returns a NEW list, original untouched
reversed_list = my_list[::-1]
print("Original list:", my_list)
print("1. Reversed list:", reversed_list)

# Order 2: ascending, using sorted() -> returns a NEW list, original untouched
print("2. Sorted ascending:", sorted(my_list))

# Order 3: descending, using sorted(reverse=True) -> returns a NEW list
print("3. Sorted descending:", sorted(my_list, reverse=True))

# Order 4: double reversed -> back to the original order
print("4. Back to original order:", my_list[::-1][::-1])

# Prove the original list is unchanged
print("Final original list:", my_list)


