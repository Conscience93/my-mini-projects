
## Challenges: Recursion

def fac(index):
    if (index == 1):
        return index
    else:
        return index * fac(index - 1)

print(fac(3))
print(fac(4))

def fib(index):
    if (index <= 1):
        return index
    else:
        return fib(index - 1) + fib(index - 2)

print(fib(6))
print(fib(8))

## Challenge: Regex

# (\d){4}-(\d){4}-(\d){4}-(\d){4}
# [^\d\s]
# \d

## challenge 3
import re

my_string = "hello"
my_string2 = "how are you"

print(re.sub("[aeiou]", "*", my_string))
print(re.sub("[aeiou]", "*", my_string2))

## challenge 4
def hide_serial(string):
    print(re.sub("\d{6}-\d{2}", "XXXXXX-XX", string))

hide_serial("123456-12-1234")   # XXXXXX-XX-1234

def hide_digits(string):
    print(re.sub("\d", "-", string))

hide_digits("You have 100 dollars") # You have --- dollars

def hide_last_four(string):
    print(re.sub("\d{4}", "****", string))

hide_last_four("12-34-5678, 90-80-7012, 45-65-1234")  # 12-34-****, 90-80-****, 45-65-****

##Challenge 5
def has_id(string):
    return True if re.search("\d{6}-\d{2}-\d{4}", string) else False

print(has_id("please don't share this: 890414-14-1422"))   # true
print(has_id("please confirm your identity: 234-122-1422"))  # false

def grab_id(string):
    return re.findall("\d{6}-\d{2}-\d{4}", string) if True else "nil"

print(grab_id("please don't share this: 890414-14-1422"))   # 890414-14-1422
print(grab_id("please confirm your identity: XXX-XX-1422"))  # nil

def grab_all_ids(string):
    return re.findall("\d{6}-\d{2}-\d{4}", string)

print(grab_all_ids("890414-14-1422, 900515-14-1092, 950616-12-5414"))  # ["890414-14-1422", "900515-14-1092", "950616-12-5414"]
print(grab_all_ids("please confirm your identity: XXX-XX-1422"))  # []

def hide_all_ids(string):
    return re.sub("\d{6}-\d{2}", "XXXXXX-XX" , string)

print(hide_all_ids("890414-14-1422, 900515-14-1092, 950616-12-5414"))  # XXXXXX-XX-1422, XXXXXX-XX-1092, XXXXXX-XX-5414
print(hide_all_ids("please confirm your identity: XXX-XX-1422"))  # please confirm your identity: XXX-XX-1422

def format_ids(string):
    return re.sub("(\d{6}).{0,1}(\d{2}).{0.1}(\d{4}")

print(format_ids("890414.14.1422, 900515141092, 950616-12-5414"))  # 890414-14-1422, 900515-14-1092, 950616-12-5414
print(format_ids("please confirm your identity: 763158581422"))  # please confirm your identity: 763158-58-1422
