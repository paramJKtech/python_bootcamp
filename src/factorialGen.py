def calculate_factorial(number : int):
    if(number == 0 or number == 1):
        return 1
    
    result = number * calculate_factorial(number - 1)
    return result
    
    
print(calculate_factorial(5))