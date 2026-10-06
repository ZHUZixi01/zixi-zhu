"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: No user input. I wrote the data myself: a name, an age, an occupation, a city and a salary, plus a dictionary that stores the same fields.
# 2. Process: Print the five values one by one, build a dictionary with the same fields, then change the age field in the dictionary.
# 3. Out: The five values printed separately, the dictionary, and the dictionary again after the age was updated.
# 4. My object, my five fields, and why those: A person record. I chose name, age, occupation, city and salary because these are the fields I would really need to describe a person at work.


# Your code below
name = "John Doe"
age = 30
occupation = "Software Engineer"
city = "New York"
salary = 50000

print("Name: " + name)
print(f"Age: {age}")
print(f"Occupation: {occupation}")
print(f"City: {city}")
print(f"Salary: $" + str(salary))

person = {
    "name": "Trump",
    "age": 50,
    "occupation": "President",
    "city": "Washington, D.C,",
    "salary": 4000000
}

# print the dictionary
print("Person dictionary:", person)

# update the age field
person["age"] = 51

# print the updated dictionary
print("Updated person dictionary:", person)