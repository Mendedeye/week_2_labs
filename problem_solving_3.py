#Task 1: Happy Numbers

#Sums the square of the digits in a number
def is_happy_number():
    is_happy = True
    number = 0
    user_input = input("\n\nPlease enter in a number to determine if it is a happy number or not: ")
    happy_list = []

    while is_happy == True and number != 1:
        number = digit_invariant(user_input)
        if list_checker(number, happy_list):
            is_happy = False
        else:
            list.append(number)

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
    for digit in number:
        total += pow(int(digit),2)

    return total

