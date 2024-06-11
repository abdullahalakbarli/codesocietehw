"""1) Write a function is_even(n) that returns True if the number is even, otherwise False."""
def is_even(n):
    if n % 2 == 0:
        return f"Yes, {n} is even"
    else:
        return f"No, {n} is odd"

n = int(input())
print(is_even(n))

"""2) Write a function is_prime(n) that checks if a number is prime. 
(A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
In other words, a prime number is only divisible by 1 and itself without leaving a remainder. 
Examples of prime numbers include 2, 3, 5, 7, 11, 13, 17, and so on.)"""


def finding_dividers(n):
    lst = []
    for i in range(1,n+1,1):
        if n % i == 0:
            lst.append(i)
        else:
            continue
    if len(lst) == 2:
        return True
    else:
        return False

def is_prime(n):
    if finding_dividers(n):
        return f"Yes, {n} is Prime"
    else:
        return f"No, {n} is not Prime"

n = int(input())
print(is_prime(n))

"""3) Write a Python function to multiply all the numbers in a list."""

def multiply_all_num(numbers):
    product = 1
    for i in numbers:
        product *= i
    return product

numbers = list(map(int, input().split()))

print(multiply_all_num(numbers))


"""4) Write a Python function that 
accepts a string and counts the 
number of upper and lower case letters."""

def check_inside_text(text):
    no_of_uppercases = 0
    no_of_lowercases = 0

    for i in text:
        if i.islower():
            no_of_lowercases += 1
        elif i.isupper():
            no_of_uppercases += 1
    return (f"No. of Upper case characters : {no_of_uppercases}\nNo. of Lower case characters : {no_of_lowercases}\n"
)
text = input()
print(check_inside_text(text))

"""5) Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included)"""
def squares_lst(lst):
    for i in range(len(lst)):
        lst[i] = lst[i]**2
    return lst

lst = []

for i in range(1,31):
    lst.append(i)
  
print(squares_lst(lst))

"""6) Write a function to check if a given number is an Armstrong number or not."""

def is_armstrong(n):
    length = len(str(n))
    
    triple_sum, temp_num = 0, n
    
    for i in range (length):
        triple_sum += (temp_num%10) ** length
        temp_num /= 10
    
    if  triple_sum == n:
        return f"The {n} number is Armstrong"
    else:
        return f"The {n} number is not Armstrong"

n = int(input())

print(is_armstrong(n))


"""7) Write a function that calculates the sum of digits of a given number."""
def sum_of_digits(n):
    sum = 0
    while n>0:
        sum += n%10
        n //= 10
    return sum

n = int(input())

print(sum_of_digits(n))

"""8) Write a function that finds the number of divisors of a given number."""
def divisors_of_number(n):
    lst = []
    for i in range (1,n//2+1):
        if n % i == 0:
            lst.append(i)
    lst.append(n)
    return lst

n = int(input())

print(divisors_of_number(n))

"""9) Write a function called fuel_cost that takes a distance as a required argument, km (default 50 km) and fuel cost (default $1 a litre) as optional arguments. The function should return the cost in dollars"""
def fuel_cost(car_brand, road_taken):
    car_brand.lower()
    litre = car_fuel_consumption[car_brand] * road_taken
    fuel_cost = litre * 0.59 #price of fuel per litre in azerbaijan
    return fuel_cost

car_fuel_consumption = {
    "toyota": 0.07,
    "honda": 0.08,
    "opel": 0.09,
    "bmw": 0.06,
    "mercedes": 0.07,
    "audi": 0.08,
    "volkswagen": 0.09,
    "chevrolet": 0.07,
    "nissan": 0.08,
    "tesla": 0.06,
    "subaru": 0.08,
    "jeep": 0.09,
    "lexus": 0.07,
    "hyundai": 0.08,
    "kia": 0.07,
    "volvo": 0.08,
    "mazda": 0.09,
    "porsche": 0.07,
    "ferrari": 0.06,
    "rolls-royce": 0.08,
    "jaguar": 0.09,
    "land Rover": 0.07,
    "chrysler": 0.08,
    "aston martin": 0.06,
    "maserati": 0.07,
    "bentley": 0.08,
    "bugatti": 0.09,
    "lamborghini": 0.07,
    "mclaren": 0.08,
    "fiat": 0.09,
    "alfa romeo": 0.07,
    "mini": 0.08,
    "saab": 0.07,
    "dodge": 0.08,
    "buick": 0.09,
    "lincoln": 0.07,
    "cadillac": 0.08,
    "hummer": 0.09
}

car_brand = input("Enter car brend:")
road_taken = float(input("Enter your driving distance (in kilometers): ")) #with km

print(fuel_cost(car_brand, road_taken), "$")

"""10) Write a function called hcf (ƏBOB) that takes 2 integer values and returns the highest common factor of the numbers."""
def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input())
b = int(input())

print(f"The HCF of {a} and {b} is {hcf(a, b)}")







