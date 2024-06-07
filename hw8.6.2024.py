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

