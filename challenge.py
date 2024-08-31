#number 1 sum of 2 numbers
def add_numbers(num1, num2):
    return num1 + num2

result1 = add_numbers(5,3)
print(result1)

#number 2 if a function is_even
def is_even(number):
    return number % 2 == 0 #if the reminder is 0 then it is even

result2 = is_even(6)
print(result2)

#number 3 reverse string
def reverse_string(text):
    return text[::-1]

result3 = reverse_string("Hello, user!")
print(result3)

#number 4 counts the number of vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

result4 = count_vowels("Moringa School.")
print(result4)

#number 5 factorial function
def calculate_factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

result5 = calculate_factorial(5)
print(result5)

#number 6 decorator function
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    return decorator_func(func)

# Example function to be decorated
def greet(name):
    return f"Welcome to, {name}!"

# Applying the decorator to the greet function
decorated_greet = apply_decorator(greet)

# Calling the decorated function
result6 = decorated_greet("Moringa")
print(result6)


#number 7 sequences
def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])

people = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("Diana", 22)]
sorted_people = sort_by_age(people)
print("People sorted by age:", sorted_people)

#number 8 sets and dictionaries
def merge_dicts(dict1, dict2):
    """
    This function merges two dictionaries, summing values for common keys.
    """
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

dict1 = {'apple': 20, 'banana': 51, 'orange': 8}
dict2 = {'banana': 30, 'orange': 72, 'grape': 12}

merged_dict = merge_dicts(dict1, dict2)
print("Merged dictionary:", merged_dict)

#number 9 class creation
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        #Display car info
        print(f"Car Info: {self.year} {self.make} {self.model}")
    
my_car = Car("Toyota", "Corolla", 2004)
my_car.display_info()