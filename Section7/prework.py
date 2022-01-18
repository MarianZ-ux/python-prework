#Task 7 Python Coding Questions

# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. 
# def hello_name(user_name):

def hello_name(user_name):
    print("Type your name  ")
    user_name = input()
    return user_name

    print("Hello " + hello_name(user_name).upper() + "!")

#hello_name = "Hello"
#user_name = "marian" 
#print(hello_name + " "+ user_name)

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():
#first_odds
def odd_numbers():
    for i in range(1, 101,2):
        print(i)

def odd_numbers2():
    numbers = list(range(1,101))
    for number in numbers:
        if number %2 != 0:
            print(number)
print(odd_numbers())

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. 
# def max_num_in_list(a_list):
a_list = [2,3,5,8,9]

def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num
current_max = a_list[0]

print(max_num_in_list(a_list))

#max_num_in_list = [0,11]
#test = max_num_in_list([2,3,5,8,9])

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):
def is_leap_year(a_year):
    if a_year %4 == 0 and a_year %100 != 0:
        print(f'{a_year} is a leap year')
    elif a_year %400 == 0:
        return True
    else:
        return False
print(is_leap_year(2022))


# Question 5
# Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be Boolean T/F Type. 
# def is_consecutive(a_list):
a_list = [8, 9, 4, 1, 2, 3, 4, 4, 8, 9, 1, 2, 3, 0, 1, 5, 6, 1]
a_list = [4,5,6,7]

def is_consecutive(a_list):
    total = 0
    min = float('+inf')
    max = float('-inf')
    seen = set()

    for n in a_list:
        if n in seen:
            return False
        seen.add(n)
        if n < min:
            min = n
        if n > max:
            max = n
        total += n
    if 2 * total != max * (max + 1) - min * (min - 1):
        return False
    return True
print(is_consecutive(a_list))