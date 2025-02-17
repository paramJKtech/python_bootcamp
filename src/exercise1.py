'''
Exercises: Variables, Operators, Strings
THECODEX EXERCISES - Variables, Operators, Strings (Available for download down below) 



1. Write a script that adds 15 and 30 and divides the sum by 2. Print out the answer.

2. Initialize two variables and use arithmetic operators to add, subtract, multiply, divide, and find the remainder.

3. Create a variable called name and store your name in it as a string.

4. Create three variables in one line and assign each one a different food item.

5. Print out "Hello" ten times using arithmetic operators.

6. Set your name and age variables in one line with multiple assignment

7. Create two strings and then create a third variable combining both of the two original strings.

8. Create a string and print the fourth letter of the word.

9. Create a string and print the letters from index 0 to 5.

10. Create a variable and print all the letters from the first index until the end.

'''

x, y = 15, 30
print((x + y) / 2)

print("add: %d" % (x + y))
print("difference: %d" % (x - y))
print(f"division: {x/y}") #using f-strings
print(f"remainder: {x % y}")


food1, food2, food3 = "burger", "pizza", "burrito"

# string repitition
print("hello" * 10)

name, age = "param", 22

string1 , string2 = "Hello", "World!"
result = string1 + string2

#printing the 4th letter of string
print(result[3])

#slicing
print(result[0:6])

print(result[0:])
