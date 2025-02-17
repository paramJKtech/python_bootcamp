# in python we can use place holders which are markers that are later replaced by actual values.
# use case: automatic email generation

sentence  = "%s is 15 years old."
name = "Jack"

print(sentence % name)

#we can have multiple placehokder in a single string
sentence = "%s %s is my friend."
print(sentence % ("Jack", "smith"))

# placehokder for integers
sentence = "%s is %d years old."
print(sentence % (name, 20))

#f-strings
print(f"Hello, {name}")


x, y = 5, 6
print(f"the sum of x and y is {x + y}")