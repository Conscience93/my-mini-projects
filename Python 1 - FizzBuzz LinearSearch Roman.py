## FizzBuzz

# result = int(input("Enter a number: "))

# if result % 15 == 0:
#     print("FizzBuzz")
# elif result % 5 == 0:
#     print("Buzz")
# elif result % 3 == 0:
#     print("Fizz")
# else:
#     print(result)

## Challenge: Loops
# my_numbers = range(0,100)
# for i in my_numbers:
#     if i == 57:
#         continue
#     if i % 2 == 0:
#         continue
#     print(i)

## Challenge: Loop Challenge

info = [
    ["name", "age", "pet"],
    ["Amy", "20", "bird"],
    ["John", "21", "cat"],
    ["Ash", "24", "dog"],
]

lists = []
for j in range(1,4):
    person = {}
    for i in range(0,3):
        person[info[0][i]] = info[j][i]
    lists.append(person)

class_info = {}
for x in range(0,3):
    class_info[x] = lists[x]

print(class_info)

class_info_answer = {
  "0": {"name": "Amy", "age": 20, "pet": "bird"},
  "1": {"name": "John", "age": 21, "pet": "cat"},
  "2": {"name": "Ash", "age": 24, "pet": "dog"},
}

## Challenge: Basic and Global Linear search (Search Algorithm)

def linear_search(target, my_list):
    search = 0
    for i in range(len(my_list)):
        search = my_list[i]
        if search == target:
            print(i)
            break
    if search != target:
        print("not found")

random_numbers = [6, 29, 18, 2, 72, 19, 18, 10, 37]

linear_search(18, random_numbers)  # 2 (it returns the position of the number)
linear_search(9, random_numbers)   # not found


def global_linear_search(target, my_list):
    search = ""
    result = []
    for j in range(0, len(bananas_arr)):
        search = bananas_arr[j]
        if search == target:
            result.append(j)
    print(result)

bananas_arr = list("bananas")   #  ["b", "a", "n", "a", "n", "a", "s"]
global_linear_search("a", bananas_arr)   # [1, 3, 5]

## Challenge: Binary search (Search Algorithm)
import math

def binary_search(target, my_list):
    high = len(my_list) - 1
    low = 0
    Found = False
    while not Found:
        mid = math.ceil((low + high)/2)
        mid_value = my_list[mid]
        if mid_value == target:
            Found = True
            return mid
        elif mid_value < target:
           low = mid
        elif mid_value > target:
            high = mid
        else:
            pass

print(binary_search(32, [13, 19, 24, 29, 32, 37, 43]))

## Challenge: Roman Numericals

# romanNumerals = ["I","IV","V", "IX", "X", "XL","L","XC","C","CD","D","CM","M"]
# values = [1,4,5,9,10,40,50,90,100,400,500,900,1000]

romanNumerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

result = int(input("Enter your thing for Romans: "))
result2 = ""

for i in range(len(values)):
    while result >= values[i]:
        result2 += romanNumerals[i]
        result -= values[i]

print(result2)
