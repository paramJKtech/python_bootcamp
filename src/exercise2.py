# Task 1

names = ["paramveer", "Jack", "Rohan", "Lisa"]
#print the second item
print(names[1])

print()

# Task 2
#create a list of sports
sports = ["football", "tennis", "cricket"]
#replace the second item with another sport
sports[1] = "badminton"
print(sports)

print()

# Task 3
#create a list containing number
numbers = [1,2,3,4,5,6,7]
#delete the fifth number
del numbers[4]
print(numbers)

print()

# Task 4
nums1 = [1,2,3]
nums2 = [4,5,6]

#merge the two lists
nums = nums1 + nums2
print(nums)
print()

# Task 5
# create list of numbners and find len, max and min
numbers = [0,45,90,20,100,-23,1000]
print(len(numbers))
print(max(numbers))
print(min(numbers))

print()

# Task 6
# create a dictionary of students with score and print student score
students = {"Paramveer" : 95, "Rohan" : 90, "Jack": 89}
print(students["Paramveer"])
print()

# Task 7
#  Create a dictionary with the key being names and 
# values being ages and then delete the second key/value pair.
dict2 = {"Paramveer" : 22, "Jack" : 21, "Leo" : 19}
del dict2["Jack"]
print(dict2)
print()

# Task 8
# Create a dictionary of names and ages and then print out all the keys and values
 # above code does this

# Task 9
movies = ("Spiderman", "Avengers", "Batman")
print(movies)

num_tuples = (23,54,90,1,89,456,22,56)
print(num_tuples[1:3])