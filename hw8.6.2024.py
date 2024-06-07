#homework for 8/6/2024

"""1) Get the keys from the dictionaries named *sample_dic* as a list
```
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}"""

subjects = {
    'Physics': 82,
    'Math': 65,
    'History': 75
}
keys = list(subjects.keys())
print(keys)

"""2) Get sum of all the values in a dictionary
# Input:
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75,
    'chemistry': 89,
    'GK': 50

}

# Expected Output: 361 """

points = {
    'Physics': 82,
    'Math': 65,
    'history': 75,
    'chemistry': 89,
    'GK': 50
}
sum = 0 #sum of values is equal to zero initially
for values in points.values():
    sum += values
print(sum)

"""3)Get the key of a minimum value from the following dictionary

# Input:
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

# Expected Output: Math """

subjects = {
  'Physics': 82,
  'Math': 65,
  'History': 75
}

min_num = min(subjects.values()) #finding min number in list

for key,value in subjects.items():
    if value == min_num:
        print(key) #printing key according to minimum number value

"""4) Delete a list of keys from a dictionary

# Inputs:
sample_dict = {
    "name": "Khalid",
    "age": 23,
    "salary": 1000,
    "city": "Baku"
}

# Keys to remove
keys = ["name", "salary"]

# Expected Output: {'city': 'Baku', 'age': 23}
"""

"""person_info = {
    "name": "Khalid",
    "age": 23,
    "salary": 1000,
    "city": "Baku"
}
keys = ["name", "salary"] #should remove these keys

for key in person_info.keys():
    if key in keys:
        person_info.pop(key)
print(person_info)""" #this code not worked. Error below:
#RuntimeError: dictionary changed size during iteration

#made some changes in code then worked
person_info = {
    "name": "Khalid",
    "age": 23,
    "salary": 1000,
    "city": "Baku"
}
removing_keys = ["name", "salary"] #should remove these keys

for key in removing_keys:
    if key in person_info:
        person_info.pop(key)
print(person_info) #why? i understand halfly

"""6) Take 10 integers from keyboard using loop and print their average value on the screen."""
loop , sum = 0 , 0
while loop < 10:
    loop += 1
    a = int(input("Enter a number: "))
    sum +=a
print(f"The avarage of {loop} numbers is {sum/loop}")

"""7) Print multiplication table of 24 using loop"""
loop = 0
while loop <= 24:
    print(f"{loop} * 24 = {loop * 24}")
    loop +=1

"""8) Factorial of any number n is represented by n! and is equal to 123....(n-1)*n.
Write a program to calculate factorial of a number.""""
def formula(number):
    temp_num = number
    dustur = ''
    while temp_num > 0:
        dustur += str(temp_num) + '*'
        temp_num -= 1
    return dustur.strip('*')

def factorial(number):
    temp_num = number
    result = 1
    while temp_num > 0:
        result *= temp_num
        temp_num -= 1
    return result

number = int(input())
while number > 0:
    print(f"{number}! = {formula(number)} = {factorial(number)}")
    number -= 1
"""9) Write a program that calculates the sum of the digits of a given number. Ask the user to input a number"""

n = int(input("Enter the number please: ")) #we get number from user
len_of_number = len(str(n)) #finding length of number
sum = 0
while len_of_number != 0:
    sum += n%10
    n //= 10
    len_of_number -= 1
print(sum)

"""10) Write a Python program that takes a string input from the user and counts the number of characters in the string."""

sentence = input()
count = 0
number_list = ['0','1','2','3','4','5','6','7','8','9']
for i in list(sentence):
    if i in number_list:
        count += 1
print(count)
