"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A single sentence typed by the user (text)
# 2. Process: Store the sentence, then apply four different string methods to it: strip, upper, lower, capitalize
# 3. Out: Four lines, each showing a different transformed version of the sentence.
# 4. My four transformations, and when each is useful:
# strip(): remove spaces at both ends, useful when cleaning user input.
# upper(): make everything uppercase, useful for headings or codes.
# lower(): make everything lowercase, useful for emails or usernames.
# capitalize(): uppercase the first letter only, useful for names or titles.


# Your code below
# Ask the user for a sentence
sentence = input("Enter a sentence: ")

# 1. Remove spaces from both ends
stripped = sentence.strip()

# 2. Make the whole sentence uppercase
upper = sentence.upper()

# 3. Make the whole sentence lowercase
lower = sentence.lower()

# 4. Capitalise the first letter of the sentence
capitalized = sentence.capitalize()

# Show all four results
print("Original:     [" + sentence + "]")
print("Stripped:     [" + stripped + "]")
print("Uppercase:    [" + upper + "]")
print("Lowercase:    [" + lower + "]")
print("Capitalized:  [" + capitalized + "]")
