"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The list I built in exercise 4.0: [5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7]. No user input.
# 2. Process: Loop through every item, find its position in the list with .index(), and compute its square (item ** 2).
# 3. Out: One line per item, showing the item, its position and its square.
# 4. What I compute for each item, and why it is worth showing: I compute the square of each number. The reader can see the item, where it sits in the list, and how big it becomes when squared, which makes it easy to compare the items at a glance.


# Your code below
list = [5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7]

i = list[0]
print(i)
print(list.index(i))
print(i**2)

item2 = list[1]
print(item2)
print(list.index(item2))
print(item2**2)


# using for loop to iterate through the list and print the item, its positon, and its square
for i in list:
    print("The item is:", i, "and its position in the list is:", list.index(i), "and the square of the item is:",i**2)


