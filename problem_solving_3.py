#Task 1: Happy Numbers

#Sums the square of the digits in a number
def is_happy_number():
    is_happy = True
    user_input = input("\n\nPlease enter in a number to determine if it is a happy number or not: ")
    number = user_input
    happy_list = []

    while is_happy == True and number != 1:
        number = digit_invariant(number)
        if list_checker(number, happy_list):
            is_happy = False
        else:
            happy_list.append(number)

    return user_input, is_happy

#Determines if a number is in a given list
def list_checker (number, list):
    in_list = False
    index = 0

    while in_list == False and index < len(list):
        if number == list[index]:
            in_list = True
        else:
            index += 1

    return in_list

def digit_invariant(number):
    total = 0
    for digit in str(number):
        total += pow(int(digit),2)

    return total

def run_happy_numbers():
    user_input, is_happy = is_happy_number()

    if is_happy == True:
        print(f"{user_input} is a happy number!!!")
    else:
        print(f"{user_input} is not a happy number. :(")

run_happy_numbers()